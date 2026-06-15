from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

# Load Model

model = pickle.load(
    open("model.pkl", "rb")
)

symptoms_df = pd.read_csv(
    "dataset/symptoms.csv"
)

all_symptoms = list(
    symptoms_df.columns[:-1]
)

app = FastAPI(
    title="Healthcare AI API"
)

# Request Model

class SymptomRequest(BaseModel):

    symptoms: list


@app.get("/")
def home():

    return {
        "message":
        "Healthcare AI API Running"
    }


@app.post("/predict")
def predict_disease(
    request: SymptomRequest
):

    input_data = [0] * len(
        all_symptoms
    )

    for symptom in request.symptoms:

        if symptom in all_symptoms:

            index = all_symptoms.index(
                symptom
            )

            input_data[index] = 1

    prediction = model.predict(
        [input_data]
    )[0]

    probabilities = model.predict_proba(
        [input_data]
    )[0]

    confidence = float(
        max(probabilities) * 100
    )

    return {

        "predicted_disease":
        prediction,

        "confidence":
        round(confidence, 2)

    }