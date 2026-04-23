# Simulating a batch ETL pipeline similar to AWS Glue / cloud-based 
import pandas as pd

print("Starting ETL Pipeline...")

# Extract
df = pd.read_csv("data/raw/sales_data.csv")
print("\nRaw Data:")
print(df)

# Transform
df["date"] = pd.to_datetime(df["date"])
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month

# Load
df.to_csv("data/processed/cleaned_data.csv", index=False)

print("\nTransformed Data:")
print(df)

print("\nETL Pipeline completed successfully!")