import pandas as pd


def churn_rate(df: pd.DataFrame) -> float:
    """Overall churn rate"""
    rate = df["churn"].mean()
    print(f"[METRIC] Overall Churn Rate: {rate:.2%}")
    return rate


def churn_by_column(df: pd.DataFrame, column: str) -> pd.DataFrame:
    """
    Churn rate grouped by a categorical column
    """
    result = df.groupby(column)["churn"].mean().sort_values(ascending=False)

    print(f"\n[METRIC] Churn by {column}")
    print(result)

    return result


def high_risk_percentage(df: pd.DataFrame) -> float:
    """Percentage of high-risk customers"""
    if "ishighrisk" in df.columns:
        rate = df["ishighrisk"].mean()
        print(f"\n[METRIC] High Risk %: {rate:.2%}")
        return rate
    else:
        print("[WARN] isHighRisk column not found")
        return 0.0


def engagement_vs_churn(df: pd.DataFrame) -> pd.DataFrame:
    """Compare engagement vs churn"""
    result = df.groupby("churn")["engagement_score"].mean()

    print("\n[METRIC] Engagement vs Churn")
    print(result)

    return result