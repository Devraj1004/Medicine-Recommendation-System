# import pandas as pd
# import joblib
# from sklearn.metrics import accuracy_score

# model = joblib.load("disease_model.pkl")

# test_df = pd.read_csv(r"C:\Users\Devra\Medicine_Recommendation_System\Data\Testing.csv")

# X_test = test_df.drop("prognosis", axis=1)
# y_test = test_df["prognosis"]

# predictions = model.predict(X_test)

# print("Model Accuracy:", accuracy_score(y_test, predictions))
import pandas as pd
import joblib

model = joblib.load("disease_model.pkl")
feature_names = joblib.load("feature_names.pkl")

test_df = pd.read_csv(r"C:\Users\Devra\Medicine_Recommendation_System\Data\Testing.csv")

# DROP unwanted column
test_df = test_df.loc[:, ~test_df.columns.str.contains("^Unnamed")]

X_test = test_df.drop("prognosis", axis=1)

# ENSURE SAME FEATURE ORDER
X_test = X_test[feature_names]

predictions = model.predict(X_test)

print("Predictions successful")
