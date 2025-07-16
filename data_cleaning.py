import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder

# Load dataset
df = pd.read_excel("Cervical Cancer Datasets_.xlsx",
                   sheet_name="Cervical Cancer Risk Factors")

# Drop unnecessary columns
df = df.drop(columns=["Patient ID", "Region",
             "Insurance Covered", "Unnamed: 12"], errors='ignore')

# Clean up column names
df.columns = df.columns.str.strip().str.replace(" ", "_").str.replace("-", "_")

# Convert Yes/No fields to binary 1/0
binary_columns = [
    "HPV_Test_Result",
    "Pap_Smear_Result",
    "Smoking_Status",
    "STDs_History",
]

for col in binary_columns:
    df[col] = df[col].map({"Y": 1, "N": 0, "POSITIVE": 1, "NEGATIVE": 0}).fillna(0)

# One-hot encode categorical variables
df = pd.get_dummies(df, columns=["Screening_Type_Last"], prefix="Test", dtype='int')

# Encode the target column - Recommended_Action
target_col = "Recommended_Action"
le = LabelEncoder()
df[target_col] = le.fit_transform(df[target_col])

# Split into features (X) and target (y)
X = df.drop(columns=[target_col])
y = df[target_col]

# Save cleaned data to CSV 
X.to_csv("X_clean.csv", index=False)
y.to_csv("y_clean.csv", index=False)

# Save label mappings and encoder
pd.Series(le.classes_).to_csv("recommended_action_labels.csv", index=False)

with open("label_encoder.pkl", "wb") as f:
    pickle.dump(le, f)

print("Data cleaned and saved as:")
print("- X_clean.csv")
print("- y_clean.csv")
print("- recommended_action_labels.csv")
print("Recommended Action Classes:", le.classes_)
