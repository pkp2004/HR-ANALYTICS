import pandas as pd
import numpy as np

# Setting seed for reproducibility
np.random.seed(42)

# Generating synthetic HR dataset
num_employees = 200

# Employee attributes
employee_id = np.arange(1, num_employees + 1)
age = np.random.randint(22, 60, num_employees)
gender = np.random.choice(["Male", "Female", "Non-Binary"], num_employees, p=[0.5, 0.45, 0.05])
department = np.random.choice(["IT", "HR", "Finance", "Marketing", "Sales", "Operations"], num_employees)
education_level = np.random.choice(["High School", "Bachelor's", "Master's", "PhD"], num_employees, p=[0.2, 0.5, 0.25, 0.05])
experience_years = np.random.randint(0, 40, num_employees)
salary = np.random.randint(30000, 150000, num_employees)
performance_score = np.random.randint(1, 5, num_employees)  # Rating from 1 to 5
attrition = np.random.choice(["Yes", "No"], num_employees, p=[0.2, 0.8])  # Employee leaving or staying

# Creating DataFrame
hr_data = pd.DataFrame({
    "Employee_ID": employee_id,
    "Age": age,
    "Gender": gender,
    "Department": department,
    "Education_Level": education_level,
    "Experience_Years": experience_years,
    "Salary": salary,
    "Performance_Score": performance_score,
    "Attrition": attrition
})

# Display first few rows
print(hr_data.head())
import matplotlib.pyplot as plt
import seaborn as sns

# Set style
sns.set_style("whitegrid")

# Attrition count plot
plt.figure(figsize=(6, 4))
sns.countplot(data=hr_data, x="Attrition", palette="coolwarm")
plt.title("Employee Attrition Count")
plt.show()

# Salary distribution by department
plt.figure(figsize=(10, 5))
sns.boxplot(data=hr_data, x="Department", y="Salary", palette="Set2")
plt.xticks(rotation=45)
plt.title("Salary Distribution by Department")
plt.show()

# Performance Score vs Attrition
plt.figure(figsize=(6, 4))
sns.boxplot(data=hr_data, x="Attrition", y="Performance_Score", palette="pastel")
plt.title("Performance Score vs Attrition")
plt.show()
