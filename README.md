# 🏥 Personalized Healthcare & Medicine Recommendation System

🌐 Live Demo

🔗 Application Link:
https://personalizedhealthcarerecommendationsystem-fkxo2z7xuv8anayuh62.streamlit.app/

## 📌 Overview

The Personalized Healthcare & Medicine Recommendation System is an AI-powered healthcare application that predicts diseases based on user symptoms and provides personalized healthcare recommendations.

The system allows users to:

- Register and Login securely
- Enter symptoms manually or through text input
- Predict possible diseases using Machine Learning
- View confidence scores and top predictions
- Receive medicine recommendations
- Get diet and workout suggestions
- Download health reports as PDF
- Track prediction history
- View analytics dashboards and visualizations

---

## 🚀 Features

### 🔐 User Authentication
- User Registration
- User Login
- Password Hashing (SHA-256)
- Session Management
- Logout Functionality

### 🤖 Disease Prediction
- Machine Learning-based prediction
- Random Forest Classifier
- Confidence Score
- Top 3 Disease Predictions

### 🧠 NLP Symptom Detection
Users can type symptoms naturally:

Example:

```text
I have fever, headache and cough
```

Automatically detected:

```text
fever
headache
cough
```

### 💊 Personalized Recommendations
- Medication Suggestions
- Diet Plans
- Workout Recommendations
- Precautions
- Doctor Recommendations

### 📄 PDF Health Report
Generate and download a complete healthcare report including:

- Disease Prediction
- Confidence Score
- Risk Level
- Medication
- Diet Plan
- Workout Plan
- Precautions
- Doctor Recommendation

### 📊 Analytics Dashboard
- Prediction History
- Disease Distribution
- Risk Level Distribution
- Feature Importance Dashboard
- Average Confidence Analysis

---

## 🛠️ Tech Stack

### Frontend
- Streamlit

### Machine Learning
- Scikit-Learn
- Random Forest Classifier

### Backend
- Python

### Database
- SQLite

### Data Processing
- Pandas
- NumPy

### Visualization
- Plotly

### PDF Generation
- ReportLab

---

## 📂 Project Structure

```text
Healthcare_Project/
│
├── app.py
├── auth.py
├── database.py
├── helper.py
├── report_generator.py
├── model.pkl
│
├── dataset/
│   └── symptoms.csv
│
├── healthcare.db
│
├── requirements.txt
└── README.md
```

---

## ⚙️ System Architecture

```text
User
  ↓
Streamlit Frontend
  ↓
Symptom Input
  ↓
Feature Engineering
  ↓
Random Forest Model
  ↓
Disease Prediction
  ↓
Recommendations
  ↓
SQLite Database
  ↓
Analytics Dashboard
```

---

## 🔍 Machine Learning Workflow

### Step 1: Symptom Collection
Users provide symptoms through:

- Manual Selection
- NLP Text Input

### Step 2: Feature Engineering

Symptoms are converted into binary vectors:

```text
Fever = 1
Headache = 1
Cough = 0
Vomiting = 0
```

### Step 3: Disease Prediction

The Random Forest Classifier predicts:

- Disease Name
- Confidence Score
- Top 3 Predictions

### Step 4: Recommendation Generation

The system generates:

- Medicines
- Diet Plans
- Workout Plans
- Precautions
- Doctor Recommendations

---

## 📈 Feature Importance Dashboard

The application displays the most influential symptoms used by the Random Forest model for prediction.

This improves model interpretability and transparency.

---

## 🗄️ Database Design

### Users Table

| Column | Description |
|----------|-------------|
| id | User ID |
| username | Username |
| password | Hashed Password |

### Prediction History Table

| Column | Description |
|----------|-------------|
| id | Prediction ID |
| username | Username |
| date | Prediction Date |
| symptoms | Selected Symptoms |
| disease | Predicted Disease |
| confidence | Confidence Score |
| risk_level | Risk Category |

---

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/RishithThanniru/Personalized_Healthcare_Recommendation_System.git
```

### Move into Project

```bash
cd Personalized_Healthcare_Recommendation_System
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
streamlit run app.py
```

---

## 📋 Requirements

```txt
streamlit
pandas
numpy
scikit-learn
plotly
reportlab
```

---

## 🎯 Key Highlights

✅ Machine Learning Disease Prediction

✅ Feature Engineering

✅ NLP Symptom Detection

✅ User Authentication

✅ SQLite Database Integration

✅ PDF Report Generation

✅ Analytics Dashboard

✅ Feature Importance Visualization

✅ User-Specific Prediction History

✅ Streamlit Web Application

---

## 🔮 Future Enhancements

- Advanced NLP using spaCy/BERT
- Medical Chatbot Integration
- Cloud Database Support
- Mobile Application
- Real-Time Doctor Consultation
- Deep Learning Models

---

## 👨‍💻 Author

**Rishith Thanniru**

B.Tech Artificial Intelligence & Machine Learning

Guru Nanak Institute of Technology

GitHub:
https://github.com/RishithThanniru

---

## ⭐ Project Summary

This project demonstrates the practical application of Machine Learning, Data Analytics, Authentication Systems, Database Management, and Healthcare Technology by providing an intelligent disease prediction and healthcare recommendation platform.
