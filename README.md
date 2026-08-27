# Titanic Dataset Cleaning

This is a beginner-friendly Python project for cleaning the Titanic dataset.

## What this project does

- Loads the Titanic dataset using Pandas
- Shows the first few rows of the dataset
- Checks the dataset shape and column names
- Finds missing values
- Removes the `Cabin` column because it has many missing values
- Fills missing `Age` values with the median age
- Fills missing `Embarked` values with the most common value
- Checks and removes duplicate rows
- Displays dataset information and numerical summary statistics

## Libraries Used

- Pandas
- NumPy
- Matplotlib
- Seaborn

## Installation

Install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

## How to Run

1. Download the Titanic dataset and name it `Titanic-Dataset.csv`.
2. Keep the CSV file in the same folder as your Python file.
3. Run the Python file:

```bash
python your_file_name.py
```

## Dataset Cleaning Steps

The project removes the `Cabin` column, fills missing values in `Age` and `Embarked`, and removes duplicate records. After cleaning, it shows the updated dataset details and statistical summary.

## Output

The program prints dataset information, missing-value counts, duplicate-row counts, and summary statistics in the terminal.
