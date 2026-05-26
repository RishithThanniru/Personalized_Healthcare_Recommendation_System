import pandas as pd

# ---------- LOAD DATASETS ----------

description = pd.read_csv(
    "dataset/description.csv"
)

medications = pd.read_csv(
    "dataset/medications.csv"
)

diets = pd.read_csv(
    "dataset/diets.csv"
)

precautions = pd.read_csv(
    "dataset/precautions.csv"
)

severity = pd.read_csv(
    "dataset/Symptom-severity.csv"
)

workout = pd.read_csv(
    "dataset/workout.csv"
)

doctor_df = pd.read_csv(
    "dataset/Doctor_Specialist.csv"
)

# ---------- DESCRIPTION ----------

def get_description(disease):

    row = description[
        description["Disease"]==disease
    ]

    if not row.empty:

        return row.iloc[0]["Description"]

    return "No description found"

# ---------- MEDICATION ----------

def get_medication(disease):

    row = medications[
        medications["Disease"]==disease
    ]

    if not row.empty:

        return row.iloc[0]["Medication"]

    return "No medication found"

# ---------- DIET ----------

def get_diet(disease):

    row = diets[
        diets["Disease"]==disease
    ]

    if not row.empty:

        return row.iloc[0]["Diet"]

    return "No diet found"

# ---------- PRECAUTIONS ----------

def get_precautions(disease):

    row = precautions[
        precautions["Disease"]==disease
    ]

    if not row.empty:

        return [

            row.iloc[0]["Precaution_1"],
            row.iloc[0]["Precaution_2"],
            row.iloc[0]["Precaution_3"],
            row.iloc[0]["Precaution_4"]

        ]

    return []

# ---------- WORKOUT ----------

def get_workout(disease):

    row = workout[
        workout["disease"]==disease
    ]

    if not row.empty:

        return row.iloc[0]["workout"]

    return "No workout found"

# ---------- SEVERITY SCORE ----------

def get_severity_score(symptoms):

    score = 0

    for symptom in symptoms:

        row = severity[
            severity["Symptom"]==symptom
        ]

        if not row.empty:

            score += int(
                row.iloc[0]["weight"]
            )

    return score

# ---------- RISK LEVEL ----------

def get_risk_level(score):

    if score < 10:

        return "LOW"

    elif score < 20:

        return "MEDIUM"

    else:

        return "HIGH"

# ---------- DOCTOR RECOMMENDATION ----------

def get_doctor(disease):

    doctor_df = pd.read_csv(
        "dataset/Doctor_Specialist.csv"
    )

    row = doctor_df[
        doctor_df["Disease"]==disease
    ]

    if not row.empty:

        return row.iloc[0][
            "Doctor_Specialist"
        ]

    return "General Physician"