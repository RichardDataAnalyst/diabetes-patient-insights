# 🩺 Diabetes Patient Health Insights Dashboard

**Portfolio Project by Richard**  
Medical Student & Health Data Analyst

## Overview
End-to-end analysis of the Pima Indians Diabetes dataset. I applied clinical reasoning together with data science tools to identify risk patterns and create actionable visualizations.

## Tech Stack
- Python (Pandas, NumPy)
- Visualization: Matplotlib & Seaborn

## Clinical Methodology
- **Data Imputation**: Treated non-biological zeros (Insulin, Glucose, BMI, etc.) as missing values and replaced them with **group-based median imputation** (diabetic vs non-diabetic) to avoid mean-bias.
- **Feature Engineering**: Developed a custom **Diabetes Risk Score** algorithm based on Glucose, BMI, Age, and Pregnancies to prioritize high-risk patients.

## Key Insights
- Strong positive correlation between Glucose levels and BMI
- Engineered risk score successfully flags high-risk patients
- Clear visual identification of risk distribution

## Visualizations
![Diabetes Dashboard]
<img width="1536" height="754" alt="1000082473" src="https://github.com/user-attachments/assets/9f15d588-94bf-4817-b4ce-099f514248f1" />

## Files
- `diabetes_patient_report.csv` – full cleaned dataset + risk scores

---
Built by a medical student with real clinical domain knowledge.
