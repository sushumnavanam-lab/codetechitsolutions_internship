# Machine Learing Model Implementation

## 📌 Overview
This project implements a **machine learning pipeline** to classify emails as **spam (1)** or **ham (0)** using word frequency features.  
The baseline model is **Logistic Regression**, with comparisons to **Naive Bayes** and **Random Forest**.

---

---

## ⚙️ Modules
1. **Import Libraries** – load required Python packages.  
2. **Load Dataset** – read `emails.csv`.  
3. **Explore Dataset** – inspect columns, data types, and class distribution.  
4. **Preprocess Data** – handle missing values.  
5. **Feature Extraction** – drop non‑numeric identifiers (`Email No.`), keep numeric word features, set target (`Prediction`).  
6. **Train/Test Split** – split dataset into training and testing sets.  
7. **Model Training** – train Logistic Regression.  
8. **Evaluation** – compute accuracy, classification report, and confusion matrix.  
9. **Save Model** – export trained model as `email_model.pkl`.  
10. **Prediction on New Emails** – test model on single email input.  
11. **Batch Predictions** – predict multiple emails at once.  
12. **Alternative Models** – compare Naive Bayes and Random Forest.

---

## 📊 Outputs
- **Accuracy score**  
- **Classification report** (precision, recall, F1)  
- **Confusion matrix heatmap** (saved in `task4/reports/confusion_matrix.png`)  
- **Saved model** (`task4/models/email_model.pkl`)  
- **Predictions** for single and batch emails  
- **Accuracy comparison** across Logistic Regression, Naive Bayes, and Random Forest  

---

## ▶️ How to Run
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
Run the notebooks step by step (task4/notebooks/).

Check outputs in:

task4/reports/confusion_matrix.png

task4/models/email_model.pkl"# codetechitsolutions_internship" 
