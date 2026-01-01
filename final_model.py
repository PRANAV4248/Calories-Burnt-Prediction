# Importing necessary libraries and functions
import pandas as pd
from xgboost import XGBRegressor
import joblib

# Importing and splitting dataset
df = pd.read_csv("data_without_outliers.csv", index_col=0)
X = df.drop(columns=["Calories"])
y = df["Calories"]

# Fitiing the model
model = XGBRegressor(n_estimators=300,
        learning_rate=0.05,
        max_depth=6,
        subsample=0.8,
        colsample_bytree=0.8,
        objective="reg:squarederror",
        random_state=42)
model.fit(X,y)

# Saving the model
joblib.dump(model, "model.pkl")
print("The model has been trained successfully!")