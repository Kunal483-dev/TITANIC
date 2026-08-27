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