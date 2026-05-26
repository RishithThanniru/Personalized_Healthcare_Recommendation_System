import pandas as pd
import pickle
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix
)

from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

# ---------- LOAD DATA ----------

df = pd.read_csv("dataset/symptoms.csv")

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

# ---------- TRAIN TEST SPLIT ----------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# ---------- MODELS ----------

models = {

    "Random Forest":
    RandomForestClassifier(),

    "Decision Tree":
    DecisionTreeClassifier(),

    "Naive Bayes":
    GaussianNB(),

    "SVM":
    SVC(probability=True)

}

results = {}

# ---------- TRAIN + EVALUATE ----------

for name, model in models.items():

    model.fit(X_train,y_train)

    predictions = model.predict(X_test)

    accuracy = accuracy_score(
        y_test,
        predictions
    )

    precision = precision_score(
        y_test,
        predictions,
        average="weighted"
    )

    recall = recall_score(
        y_test,
        predictions,
        average="weighted"
    )

    f1 = f1_score(
        y_test,
        predictions,
        average="weighted"
    )

    results[name] = {

        "Accuracy":accuracy,
        "Precision":precision,
        "Recall":recall,
        "F1 Score":f1

    }

# ---------- MODEL COMPARISON ----------

results_df = pd.DataFrame(results).T

print("\nMODEL COMPARISON\n")

print(results_df)

# ---------- BEST MODEL ----------

best_model_name = results_df["Accuracy"].idxmax()

print("\nBest Model:",best_model_name)

best_model = models[best_model_name]

# ---------- SAVE MODEL ----------

pickle.dump(
    best_model,
    open("model.pkl","wb")
)

print("\nModel Saved Successfully!")

# ---------- CONFUSION MATRIX ----------

pred = best_model.predict(X_test)

cm = confusion_matrix(
    y_test,
    pred
)

plt.figure(figsize=(10,8))

sns.heatmap(
    cm,
    cmap="Blues"
)

plt.title(
    f"Confusion Matrix - {best_model_name}"
)

plt.show()

# ---------- ACCURACY GRAPH ----------

results_df["Accuracy"].plot(
    kind="bar",
    figsize=(8,5),
    color="green"
)

plt.title(
    "Model Accuracy Comparison"
)

plt.ylabel(
    "Accuracy"
)

plt.show()

# ---------- FEATURE IMPORTANCE ----------

if hasattr(
    best_model,
    "feature_importances_"
):

    feature_importance = best_model.feature_importances_

    features = X.columns

    importance_df = pd.DataFrame({

        "Symptom":features,
        "Importance":feature_importance

    })

    top_features = importance_df.sort_values(
        by="Importance",
        ascending=False
    ).head(10)

    print(
        "\nTOP IMPORTANT SYMPTOMS\n"
    )

    print(
        top_features
    )

    plt.figure(figsize=(10,6))

    plt.barh(

        top_features["Symptom"],
        top_features["Importance"]

    )

    plt.title(
        "Top 10 Important Symptoms"
    )

    plt.xlabel(
        "Importance Score"
    )

    plt.show()

# ---------- EDA SECTION ----------

print(
    "\nDATASET SHAPE:"
)

print(
    df.shape
)

print(
    "\nDATASET INFO:"
)

print(
    df.info()
)

print(
    "\nFIRST 5 ROWS:"
)

print(
    df.head()
)

# Disease Distribution

plt.figure(
    figsize=(12,6)
)

sns.countplot(
    y=df["prognosis"]
)

plt.title(
    "Disease Distribution"
)

plt.show()

# Correlation Heatmap

plt.figure(
    figsize=(15,10)
)

sns.heatmap(

    df.iloc[:,:20].corr(),

    cmap="coolwarm"

)

plt.title(
    "Correlation Heatmap"
)

plt.show()