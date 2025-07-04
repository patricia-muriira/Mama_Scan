import pandas as pd
import numpy as np
from imblearn.over_sampling import SMOTE

# Load cleaned data
X = pd.read_csv("X_clean.csv")
y = pd.read_csv("y_clean.csv").squeeze()

# Merge into one DataFrame for easier manipulation
df = X.copy()
df["Recommended_Action"] = y

MIN_COUNT = 2  # minimum samples for SMOTE to work properly

# Manual augmentation for classes with < MIN_COUNT samples
class_counts = df["Recommended_Action"].value_counts()
augmented_rows = []

for label, count in class_counts.items():
    if count < MIN_COUNT:
        needed = MIN_COUNT - count
        sample = df[df["Recommended_Action"] == label]

        for _ in range(needed):
            new_row = sample.sample(n=1).copy()
            numeric_cols = new_row.select_dtypes(include=np.number).columns.drop("Recommended_Action")
            for col in numeric_cols:
                new_row[col] += np.random.normal(0, 0.1)
            augmented_rows.append(new_row)

if augmented_rows:
    df_augmented = pd.concat([df] + augmented_rows, ignore_index=True)
else:
    df_augmented = df

# Separate features and target again
X_aug = df_augmented.drop(columns="Recommended_Action")
y_aug = df_augmented["Recommended_Action"]

# Apply SMOTE to balance dataset
smote = SMOTE(sampling_strategy='not majority', k_neighbors=1, random_state=42)
X_final, y_final = smote.fit_resample(X_aug, y_aug)

# Save the final augmented and balanced data
X_final.to_csv("X_final.csv", index=False)
y_final.to_csv("y_final.csv", index=False)

print("Final class distribution:")
print(pd.Series(y_final).value_counts().sort_index())
