import pandas as pd
import matplotlib.pyplot as plt

# Load processed data
df = pd.read_csv("data/processed/cleaned_data.csv")

# Aggregate revenue by product
revenue = df.groupby("product")["amount"].sum()

# Plot chart
plt.figure(figsize=(6,4))
revenue.plot(kind="bar")

plt.title("Revenue by Product")
plt.xlabel("Product")
plt.ylabel("Revenue")

# Save image
plt.tight_layout()
plt.savefig("dashboards/revenue_by_product.png")

print("Chart generated successfully!")