import streamlit as st
import pickle
import pandas as pd
from report_generator import *
import plotly.express as px
from auth import register_user, login_user

from datetime import datetime

from helper import *
from database import *

# ---------- LOAD MODEL ----------

model = pickle.load(
    open("model.pkl","rb")
)

# ---------- LOAD SYMPTOMS ----------

symptoms_df = pd.read_csv(
    "dataset/symptoms.csv"
)

all_symptoms = list(
    symptoms_df.columns[:-1]
)

# ---------- PAGE ----------

st.set_page_config(

    page_title="Healthcare AI System",

    layout="wide"

)

# ---------- CUSTOM CSS ----------

st.markdown("""

<style>

.main {
    padding-top: 1rem;
}

.stButton button {
    width: 100%;
    border-radius: 10px;
    height: 45px;
}

.stTextInput input {
    border-radius: 10px;
}

.login-box {
    padding: 20px;
    border-radius: 15px;
    background-color: #f8f9fa;
}

</style>

""", unsafe_allow_html=True)

# ---------- APP HEADER ----------

st.markdown(

    """
    <h1 style='text-align:center;color:#0E76A8'>
    🏥 Personalized Healthcare & Medicine Recommendation System
    </h1>
    """,

    unsafe_allow_html=True

)

# ---------- LOGIN SYSTEM ----------

menu = [

    "🔐 Login",

    "📝 Register"

]

choice = st.sidebar.selectbox(

    "Account",

    menu

)

# ---------- REGISTER ----------

if choice == "📝 Register":

    st.markdown("## 📝 Create New Account")

    new_user = st.text_input(

        "👤 Username"

    )

    new_password = st.text_input(

        "🔒 Password",

        type="password"

    )

    if st.button(

        "🚀 Register"

    ):

        success = register_user(

            new_user,

            new_password

        )

        if success:

            st.success(

                "✅ Account Created Successfully"

            )

        else:

            st.error(

                "❌ Username Already Exists"

            )

    st.stop()

# ---------- LOGIN ----------

if choice == "🔐 Login":

    st.markdown("## 🔐 Login")

    username = st.text_input(

        "👤 Username"

    )

    password = st.text_input(

        "🔒 Password",

        type="password"

    )

    if st.button(

        "🚀 Login"

    ):

        user = login_user(

            username,

            password

        )

        if user:

            st.session_state[
                "logged_in"
            ] = True

            st.session_state[
                "username"
            ] = username

            st.rerun()

        else:

            st.error(

                "❌ Invalid Username or Password"

            )

    if not st.session_state.get(

        "logged_in",

        False

    ):

        st.stop()

# ---------- MAIN APP ----------

st.sidebar.success(

    f"👋 Welcome {st.session_state['username']}"

)

# ---------- LOGOUT ----------

if st.sidebar.button(

    "🚪 Logout"

):

    st.session_state.clear()

    st.rerun()

st.sidebar.header(

    "Select Symptoms"

)



# ---------- NLP TEXT INPUT ----------

st.sidebar.subheader(
    "🧠 NLP Symptom Input"
)

text_input = st.sidebar.text_area(
    "Describe Symptoms"
)

# ---------- MANUAL INPUT ----------

selected_symptoms = st.sidebar.multiselect(

    "Choose Symptoms",

    all_symptoms

)

# ---------- NLP DETECTION ----------

if text_input:

    detected_symptoms = []

    user_text = text_input.lower()

    for symptom in all_symptoms:

        clean_symptom = symptom.replace(
            "_",
            " "
        ).lower()

        if clean_symptom in user_text:

            detected_symptoms.append(
                symptom
            )

    if detected_symptoms:

        selected_symptoms = list(

            set(

                selected_symptoms +

                detected_symptoms

            )

        )

        st.sidebar.success(

            f"Detected: {', '.join(detected_symptoms)}"

        )

# ---------- PREDICT ----------

if st.sidebar.button("Predict Disease"):

    # Create Input Vector

    input_data = [0] * len(all_symptoms)

    for symptom in selected_symptoms:

        index = all_symptoms.index(symptom)

        input_data[index] = 1

    # ---------- PREDICTION ----------

    prediction = model.predict(
        [input_data]
    )[0]

    probabilities = model.predict_proba(
        [input_data]
    )[0]

    confidence = max(
        probabilities
    ) * 100

    # ---------- TOP 3 PREDICTIONS ----------

    top_indices = probabilities.argsort()[-3:][::-1]

    top_predictions = []

    for idx in top_indices:

        disease = model.classes_[idx]

        prob = probabilities[idx] * 100

        top_predictions.append(

            (disease, prob)

        )

    # ---------- RISK ANALYSIS ----------

    severity_score = get_severity_score(
        selected_symptoms
    )

    risk_level = get_risk_level(
        severity_score
    )

    # ---------- SAVE HISTORY ----------

    insert_prediction(

    st.session_state["username"],

    str(datetime.now()),

    ", ".join(selected_symptoms),

    prediction,

    round(confidence, 2),

    risk_level

)

    # ---------- RESULTS ----------

    st.success(
        f"Predicted Disease : {prediction}"
    )

    st.info(
        f"Confidence Score : {confidence:.2f}%"
    )

    st.subheader(
        "📊 Top Disease Predictions"
    )

    for i, (disease, prob) in enumerate(
        top_predictions,
        start=1
    ):

        st.write(
            f"{i}. {disease} - {prob:.2f}%"
        )

    st.warning(
        f"Risk Level : {risk_level}"
    )

    col1, col2 = st.columns(2)

    # ---------- COLUMN 1 ----------

    with col1:

        st.subheader("📖 Description")

        st.write(
            get_description(
                prediction
            )
        )

        st.subheader("💊 Medication")

        st.write(
            get_medication(
                prediction
            )
        )

        st.subheader("🥗 Diet Recommendation")

        st.write(
            get_diet(
                prediction
            )
        )

        # ---------- COLUMN 2 ----------

    with col2:

        st.subheader(
            "🛡 Precautions"
        )

        precautions_list = get_precautions(
            prediction
        )

        for p in precautions_list:

            st.write(
                "✔",
                p
            )

        st.subheader(
            "🏃 Workout"
        )

        st.write(
            get_workout(
                prediction
            )
        )

        st.subheader(
            "👨‍⚕ Recommended Doctor"
        )

        st.write(
            get_doctor(
                prediction
            )
        )

        # ---------- PDF REPORT ----------

        pdf_file = generate_report(

            prediction,

            confidence,

            risk_level,

            get_description(
                prediction
            ),

            get_medication(
                prediction
            ),

            get_diet(
                prediction
            ),

            get_workout(
                prediction
            ),

            get_doctor(
                prediction
            ),

            precautions_list

        )

        with open(
            pdf_file,
            "rb"
        ) as file:

            st.download_button(

                label="📄 Download Health Report",

                data=file,

                file_name="Health_Report.pdf",

                mime="application/pdf"

            )
# ---------- HISTORY ----------

st.subheader(
    "📜 Prediction History"
)

history = get_history(
    st.session_state["username"]
)

if history:

    history_df = pd.DataFrame(

        history,

        columns=[

            "ID",
            "Username",
            "Date",
            "Symptoms",
            "Disease",
            "Confidence",
            "Risk Level"

        ]

    )

    st.dataframe(
        history_df.tail(10)
    )

    # ---------- ANALYTICS DASHBOARD ----------

    st.subheader(
        "📊 Health Analytics Dashboard"
    )

    # Total Predictions

    total_predictions = len(
        history_df
    )

    # Average Confidence

    avg_confidence = round(

        history_df[
            "Confidence"
        ].mean(),

        2

    )

    # Most Predicted Disease

    most_common_disease = history_df[
        "Disease"
    ].mode()[0]

    # Metrics

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(

            "Total Predictions",

            total_predictions

        )

    with col2:

        st.metric(

            "Average Confidence",

            f"{avg_confidence}%"

        )

    with col3:

        st.metric(

            "Most Common Disease",

            most_common_disease

        )

else:

    st.info(
        "No prediction history found."
    )
    
    # ---------- FEATURE IMPORTANCE ----------

st.subheader(
    "⭐ Feature Importance Dashboard"
)

try:

    if hasattr(model, "feature_importances_"):

        importance = model.feature_importances_

        importance_df = pd.DataFrame({

            "Symptom": all_symptoms,

            "Importance": importance

        })

        importance_df = importance_df.sort_values(

            by="Importance",

            ascending=False

        ).head(10)

        fig = px.bar(

            importance_df,

            x="Importance",

            y="Symptom",

            orientation="h",

            title="Top 10 Important Symptoms"

        )

        st.plotly_chart(

            fig,

            use_container_width=True

        )

except Exception as e:

    st.error(

        f"Feature Importance Error: {e}"

    )

# ---------- DISEASE DISTRIBUTION ----------

st.subheader(
    "📈 Disease Distribution"
)

disease_counts = history_df[
    "Disease"
].value_counts()

fig1 = px.bar(

    x=disease_counts.index,

    y=disease_counts.values,

    labels={

        "x": "Disease",

        "y": "Count"

    },

    title="Disease Frequency"

)

st.plotly_chart(
    fig1,
    use_container_width=True
)

# ---------- RISK LEVEL DISTRIBUTION ----------

st.subheader(
    "⚠ Risk Level Distribution"
)

risk_counts = history_df[
    "Risk Level"
].value_counts()

fig2 = px.pie(

    names=risk_counts.index,

    values=risk_counts.values,

    title="Risk Level Analysis"

)

st.plotly_chart(
    fig2,
    use_container_width=True
)