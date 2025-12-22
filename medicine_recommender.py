import pandas as pd

med_df = pd.read_csv(r"C:\Users\Devra\Medicine_Recommendation_System\Data\disease_to_medicine.csv")

def get_medicine(disease):
    result = med_df[med_df["Disease"].str.lower() == disease.lower()]
    if result.empty:
        return "Consult a doctor"
    return result.iloc[0]["Recommended_Medicine"]
