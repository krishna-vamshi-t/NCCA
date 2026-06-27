import pandas as pd


def segment_customers(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    def assign_segment(row):
        # High risk: payment issues or very inactive
        if row["payment_risk"] == 1 or row["activity_level"] == "churn-risk":
            return "High Risk"

        # Loyal: long tenure and high engagement
        if row["tenure_group"] in ["2-3y", "3y+"] and row["high_engagement"] == 1:
            return "Loyal"

        # Casual: moderate engagement, not at risk
        if row["high_engagement"] == 0 and row["activity_level"] == "moderate":
            return "Casual"

        # New: short tenure
        if row["tenure_group"] in ["0-6m", "6-12m"]:
            return "New"

        return "Mid-Tier"

    df["segment"] = df.apply(assign_segment, axis=1)

    # Print segment summary
    summary = df["segment"].value_counts()
    print("\n[INFO] Customer Segments:")
    print(summary)
    print(f"\n[INFO] Segment % breakdown:")
    print((summary / len(df) * 100).round(2))

    return df


def churn_by_segment(df: pd.DataFrame) -> None:
    print("\n[METRIC] Churn Rate by Segment:")
    print(df.groupby("segment")["churn"].mean().sort_values(ascending=False) * 100)