import pandas as pd
import joblib
from medicine_recommender import get_medicine

model = joblib.load("models/disease_model.pkl")
feature_names = joblib.load("models/feature_names.pkl")

# -----------------------------
# High-risk disease rules
# -----------------------------
AIDS_REQUIRED_SYMPTOMS = {
    "weight_loss",
    "extra_marital_contacts",
    "receiving_blood_transfusion",
    "receiving_unsterile_injections",
    "coma"
}

TB_REQUIRED_SYMPTOMS = {
    "chronic_cough",
    "weight_loss",
    "blood_in_sputum",
    "night_sweats"
}

HEART_ATTACK_REQUIRED = {
    "chest_pain",
    "breathlessness",
    "sweating"
}

# -----------------------------
# Helper function
# -----------------------------
def has_required(symptoms, required_set, min_count=2):
    return len(required_set.intersection(symptoms)) >= min_count


# -----------------------------
# Prediction function
# -----------------------------
def predict_disease(symptom_list):

    input_data = [1 if symptom in symptom_list else 0 for symptom in feature_names]

    if sum(input_data) < 2:
        return "Unknown", "Please enter at least 2 valid symptoms"

    df = pd.DataFrame([input_data], columns=feature_names)
    predicted_disease = model.predict(df)[0]

    symptom_set = set(symptom_list)

    # -----------------------------
    # SAFETY OVERRIDES
    # -----------------------------
    if predicted_disease == "AIDS" and not has_required(symptom_set, AIDS_REQUIRED_SYMPTOMS):
        predicted_disease = "Viral Fever"

    elif predicted_disease == "Tuberculosis" and not has_required(symptom_set, TB_REQUIRED_SYMPTOMS):
        predicted_disease = "Pneumonia"

    elif predicted_disease == "Heart attack" and not has_required(symptom_set, HEART_ATTACK_REQUIRED):
        predicted_disease = "GERD"

    medicine = get_medicine(predicted_disease)

    return predicted_disease, medicine