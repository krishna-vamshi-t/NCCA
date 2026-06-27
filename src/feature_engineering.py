import pandas as pd

def create_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    df["engagement_score"] = (
        df["watchhourspermonth"] * 0.4 +
        df["downloadspermonth"] * 0.3 +
        df["recommendationclicks"] * 0.3
    )

    df["tenure_group"] = pd.cut(
        df["tenuremonths"],
        bins=[0, 6, 12, 24, 36, 100],
        labels=["0-6m", "6-12m", "1-2y", "2-3y", "3y+"]
    )

    df["activity_level"] = pd.cut(
        df["dayssincelastlogin"],
        bins=[-1, 7, 30, 90, 1000],
        labels=["active", "moderate", "inactive", "churn-risk"]
    )

    df["payment_risk"] = (df["paymentfailures"] >= 2).astype(int)

    df["high_engagement"] = (
        df["engagement_score"] > df["engagement_score"].median()
    ).astype(int)

    print(f"[INFO] Feature engineering completed. Shape: {df.shape}")

    return df