import streamlit as st
import pickle
import pandas as pd
import os

from datetime import datetime
from helper import *

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

st.title(
"🏥 Personalized Healthcare & Medicine Recommendation System"
)

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

if st.sidebar.button(
    "Predict Disease"
):

    input_data = [0]*132

    for symptom in selected_symptoms:

        index = all_symptoms.index(
            symptom
        )

        input_data[index] = 1

    prediction = model.predict(
        [input_data]
    )[0]

    confidence = max(

        model.predict_proba(
            [input_data]
        )[0]

    )*100

    severity_score = get_severity_score(
        selected_symptoms
    )

    risk_level = get_risk_level(
        severity_score
    )

    # ---------- SAVE HISTORY ----------

    history_data = {

        "Date":[
            datetime.now()
        ],

        "Symptoms":[
            ", ".join(
                selected_symptoms
            )
        ],

        "Disease":[
            prediction
        ],

        "Confidence":[
            round(
                confidence,
                2
            )
        ],

        "Risk Level":[
            risk_level
        ]

    }

    history_df = pd.DataFrame(
        history_data
    )

    if os.path.exists(
        "prediction_history.csv"
    ):

        history_df.to_csv(

            "prediction_history.csv",

            mode="a",

            header=False,

            index=False

        )

    else:

        history_df.to_csv(

            "prediction_history.csv",

            index=False

        )

    # ---------- RESULTS ----------

    st.success(
        f"Predicted Disease : {prediction}"
    )

    st.info(
        f"Confidence Score : {confidence:.2f}%"
    )

    st.warning(
        f"Risk Level : {risk_level}"
    )

    col1,col2 = st.columns(2)

    # ---------- COLUMN 1 ----------

    with col1:

        st.subheader(
            "📖 Description"
        )

        st.write(
            get_description(
                prediction
            )
        )

        st.subheader(
            "💊 Medication"
        )

        st.write(
            get_medication(
                prediction
            )
        )

        st.subheader(
            "🥗 Diet Recommendation"
        )

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
                "✔",p
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

# ---------- HISTORY ----------

st.subheader(
    "📜 Prediction History"
)

if os.path.exists(
    "prediction_history.csv"
):

    history = pd.read_csv(
        "prediction_history.csv"
    )

    st.dataframe(
        history.tail(10)
    )