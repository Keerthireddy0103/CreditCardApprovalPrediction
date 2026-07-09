import pandas as pd
import numpy as np

# Load datasets
application = pd.read_csv("dataset/application_record.csv")
credit = pd.read_csv("dataset/credit_record.csv")

# Display first 5 rows
print("Application Dataset")
print(application.head())

print("\nCredit Dataset")
print(credit.head())

# Display shape
print("\nApplication Shape:", application.shape)
print("Credit Shape:", credit.shape)

# Display columns
print("\nApplication Columns:")
print(application.columns)

print("\nCredit Columns:")
print(credit.columns)
print(application.isnull().sum())

print(credit.isnull().sum())
