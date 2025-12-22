import pandas as pd

df = pd.read_csv(r"C:\Users\Devra\Medicine_Recommendation_System\Data\Training.csv")
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

symptoms = df.drop("prognosis", axis=1).columns.tolist()

print("Total symptoms:", len(symptoms))
for s in symptoms:
    print(s)
