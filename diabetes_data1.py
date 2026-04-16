import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ========================================================
# DIABETES PATIENT HEALTH INSIGHTS DASHBOARD
# Portfolio Project by Richard
# ========================================================

# Load the dataset
df = pd.read_csv("diabetes.csv")

print("Original dataset shape:", df.shape)

# ====================== DATA CLEANING ======================
cols_with_zeros = ['Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI']

for col in cols_with_zeros:
    df[col] = df[col].replace(0, np.nan)

# Group-based median imputation (professional medical data practice)
for col in cols_with_zeros:
    df[col] = df[col].fillna(
        df.groupby('Outcome')[col].transform('median')
    )

print("After cleaning shape:", df.shape)

# ====================== HEALTH METRICS ======================
df['BMI_Category'] = pd.cut(df['BMI'], bins=[0, 18.5, 25, 30, 100],
                            labels=['Underweight', 'Normal', 'Overweight', 'Obese'])

df['Risk_Score'] = (
    (df['Glucose'] > 140) * 3 +
    (df['BMI'] > 30) * 2 +
    (df['Age'] > 45) * 2 +
    (df['Pregnancies'] > 3) * 1
)

# ====================== SUMMARY ======================
print(f"\nTotal patients: {len(df)}")
print(f"Patients with diabetes: {len(df[df['Outcome'] == 1])}")
print(f"Average BMI: {df['BMI'].mean():.2f}")
print(f"Average Age: {df['Age'].mean():.1f} years")
print(f"High Risk patients (Risk Score >= 5): {len(df[df['Risk_Score'] >= 5])}")

# ====================== VISUALIZATIONS ======================
sns.set_style("whitegrid")
fig, axes = plt.subplots(2, 2, figsize=(12, 9))

sns.histplot(df['BMI'], kde=True, color='blue', ax=axes[0, 0])
axes[0, 0].set_title('BMI Distribution')

sns.scatterplot(data=df, x='BMI', y='Glucose', hue='Risk_Score', 
                palette='viridis', ax=axes[0, 1])
axes[0, 1].set_title('Glucose vs BMI (colored by Risk Score)')

df['Risk_Score'].value_counts().plot(kind='bar', ax=axes[1, 0])
axes[1, 0].set_title('Risk Score Distribution')

sns.boxplot(data=df, x='BMI_Category', y='Risk_Score', ax=axes[1, 1])
axes[1, 1].set_title('Risk Score by BMI Category')

plt.tight_layout()
plt.show()

# Save files
plt.savefig('diabetes_health_dashboard.png', dpi=300, bbox_inches='tight')
print("✅ Dashboard saved as 'diabetes_health_dashboard.png'")

df.to_csv("diabetes_patient_report.csv", index=False)
print("✅ Report saved as 'diabetes_patient_report.csv'")