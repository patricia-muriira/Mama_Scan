import pandas as pd

X = pd.read_csv("X_augmented.csv")

# Identify non-numeric columns
non_numeric = X.select_dtypes(exclude='number').columns

print("🧾 Non-numeric columns in X:")
print(non_numeric)

# Peek at what's inside one of them
for col in non_numeric:
    print(f"\n▶ Sample values from column '{col}':")
    print(X[col].unique()[:5])
