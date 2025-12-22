import pandas as pd
from recommender import predict_disease
from symptoms_mapper import SYMPTOM_MAP

# -----------------------------
# Load valid symptoms
# -----------------------------
df = pd.read_csv("Data/Training.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]
VALID_SYMPTOMS = set(df.drop("prognosis", axis=1).columns)

print("\n🩺 Medicine Recommendation System")
print("Type at least 3 symptoms separated by commas.")
print("Type 'exit' to quit.\n")

# -----------------------------
# MAIN LOOP
# -----------------------------
while True:
    user_input = input("> ").lower().strip()

    # Exit condition
    if user_input in ["exit", "quit"]:
        print("\n👋 Thank you for using the system. Stay healthy!")
        break

    user_input = user_input.split(",")

    mapped_symptoms = []

    for s in user_input:
        s = s.strip()

        if s in VALID_SYMPTOMS:
            mapped_symptoms.append(s)

        elif s in SYMPTOM_MAP and SYMPTOM_MAP[s] in VALID_SYMPTOMS:
            mapped_symptoms.append(SYMPTOM_MAP[s])

    # -----------------------------
    # Validation
    # -----------------------------
    if len(mapped_symptoms) < 2:
        print("\n❌ Not enough recognizable symptoms.")
        print("Please enter at least 2 clear symptoms (example: fever, cough).\n")
        continue   # 🔁 Ask again instead of exiting

    # -----------------------------
    # Prediction
    # -----------------------------
    disease, medicine = predict_disease(mapped_symptoms)

    print("\n🧠 Predicted Disease:", disease)
    print("💊 Recommended Medicine:", medicine)

    print("\n⚠ DISCLAIMER:")
    print("This system is for educational purposes only.")
    print("Always consult a certified doctor.\n")

    # Optional: Ask if user wants to continue
    again = input("Do you want to try again? (y/n): ").lower()
    if again != "y":
        print("\n👋 Thank you for using the system. Stay healthy!")
        break
