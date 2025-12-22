
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import joblib

df = pd.read_csv(r"C:\Users\Devra\Medicine_Recommendation_System\Data\Training.csv")

# DROP unwanted column
df = df.loc[:, ~df.columns.str.contains("^Unnamed")]

X = df.drop("prognosis", axis=1)
y = df["prognosis"]

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "disease_model.pkl")
joblib.dump(X.columns.tolist(), "feature_names.pkl")

print("Model trained successfully")
