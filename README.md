# 👩🏾‍⚕️ MAMA SCAN

This project focuses on **classifying and recommending actions** to clinicians and community health volunteers (CHVs) related to women's health screenings for cervical cancer.

---

## ⚙️ Setup

To set up the environment:

1. **Create a virtual environment** (optional but recommended)
2. **Install required packages**:

   ```bash
   pip install -r requirements.txt
   ```

---

## 🧹 Data Preprocessing

> 📄 Raw data source: `Cervical Cancer Datasets_.xlsx`

Preprocessing steps:

* **Column Dropping**: Removed `Patient Id`, `Region`, and `Insurance Covered`
* **One-Hot Encoding**: Applied to test types (`Pap Smear`, `VIA`, `HPV DNA`)
* **Label Encoding**: Target column `Recommended_Action` encoded into integers

**🔄 Output files:**

* `X_clean.csv`
* `y_clean.csv`
* `label_encoder.pkl`
* `recommended_action_labels.csv`

---

## ⚖️ Class Distribution Handling

### 📊 Original Class Distribution

The initial distribution of `Recommended_Action` was **imbalanced**, with some classes having only one sample — making fair train/test splits unreliable.

![Original Distribution](https://github.com/user-attachments/assets/fbe9e8bc-53ed-42da-a218-8a7f778630a9)

---

### 🖬 Augmented Class Distribution

After applying **noise injection + SMOTE**, each class was brought to **31 samples**, ensuring balance.

* **Techniques Used**: Gaussian noise + SMOTE
* **🔄 Output**:

  * `X_final.csv`
  * `y_final.csv`

![Augmented Distribution](https://github.com/user-attachments/assets/d158ebb9-37d0-40c0-8487-91956d4090ab)

---

## 🤖 Model Training & Evaluation

* **Model Type**: RandomForestClassifier (or insert your actual model type)
* **Overall Accuracy**: `0.85`
* **Macro Average**:

  * Precision: `0.86`
  * Recall: `0.85`
  * F1-Score: `0.85`
  * Support: `75`

**🔄 Output**:

* `model.pkl`

---

### 📉 Confusion Matrix Comparison

1. **Using Gaussian Noise only**
   Accuracy: `0.65`

   ![Confusion Matrix - Noise](https://github.com/user-attachments/assets/341976da-cf2b-4a91-91cd-91f36f9948f2)

2. **Using SMOTE**
   Accuracy: `0.85` — significant performance improvement

   ![Confusion Matrix - SMOTE](https://github.com/user-attachments/assets/637786d8-08e9-44f0-be0d-4e3be6077910)

3. **Classification Report with SMOTE**
   ![Classification Report](https://github.com/user-attachments/assets/7066e567-925f-4ba2-a325-3007c1eec1ce)

---

## 🌐 Streamlit Web App

You can run the prediction interface using Streamlit:

### ▶️ Local Run:

```bash
streamlit run app.py
```

### 🌍 Deployed Version:

> [Launch App](https://mamascan.streamlit.app/)

---

## 🦥 Recommendation Classes

The model maps predictions to the following **recommended actions**:

1. **For annual follow-up and Pap smear in 3 years**
2. **For biopsy and cytology** *(TAH not recommended)*
3. **For colposcopy, biopsy, and cytology**
4. **For colposcopy, biopsy, cytology ± TAH**
5. **For colposcopy, cytology, then laser therapy**
6. **For HPV vaccine and sexual education**
7. **For laser therapy**
8. **For Pap smear**
9. **For repeat HPV testing annually and Pap smear in 3 years**
10. **Repeat Pap smear in 3 years**
11. **Repeat Pap smear in 3 years and for HPV vaccine**

---
## Prediction Screenshot
![Sample Prediction](https://github.com/user-attachments/assets/462f8369-1b60-4830-9279-35f80c18edfb)
