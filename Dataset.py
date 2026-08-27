import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("Titanic-Dataset.csv")
print(df.head())
print("\nDataset shape:", df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nMissing values:")
print(df.isnull().sum())
# Cabin column mein bahut zyada missing values hain, isliye remove kar rahe hain
df = df.drop(columns=["Cabin"])

# Age numerical column hai; missing values ko median age se fill karenge
df["Age"] = df["Age"].fillna(df["Age"].median())

# Embarked categorical column hai; missing values ko most common value se fill karenge
df["Embarked"] = df["Embarked"].fillna(df["Embarked"].mode()[0])

# Cleaning verify karne ke liye
print("\nMissing values after cleaning:")
print(df.isnull().sum())
# Duplicate rows check karo
print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# Agar duplicate rows hain toh remove karo
df = df.drop_duplicates()

print("Duplicate rows after cleaning:", df.duplicated().sum())

# Har column ka data type aur non-null values dekho
print("\nDataset information after cleaning:")
df.info()

# Numerical columns ka summary
print("\nNumerical columns summary:")
print(df.describe())
# Survival count plot
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Survived", palette="Set2")
plt.title("Survival Count")
plt.xticks([0, 1], ["Not Survived", "Survived"])
plt.show()

# Gender ke according survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Sex", hue="Survived", palette="Set1")
plt.title("Survival by Gender")
plt.show()

# Passenger class ke according survival
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x="Pclass", hue="Survived", palette="Set2")
plt.title("Survival by Passenger Class")
plt.show()

# Age distribution
plt.figure(figsize=(8, 4))
sns.histplot(df["Age"], bins=30, kde=True, color="skyblue")
plt.title("Age Distribution")
plt.show()

# Fare distribution
plt.figure(figsize=(8, 4))
sns.histplot(df["Fare"], bins=30, kde=True, color="orange")
plt.title("Fare Distribution")
plt.show()

# Correlation heatmap for numerical columns
plt.figure(figsize=(8, 5))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

# Cleaned dataset save karo
df.to_csv("Titanic-Cleaned-Dataset.csv", index=False)

print("\nCleaned dataset saved as Titanic-Cleaned-Dataset.csv")


