import pandas as pd

df = pd.read_csv("data/netflix_customer_churn_dataset.csv")

print(df.head())

# Example SQL-like analysis in pandas
print("\nChurn Rate:")
print(df["Churn"].mean())

print("\nChurn by Plan:")
print(df.groupby("SubscriptionPlan")["Churn"].mean())

print("\nChurn by Country:")
print(df.groupby("Country")["Churn"].mean().sort_values(ascending=False))