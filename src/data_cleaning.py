import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    # remove duplicates
    df = df.drop_duplicates()

    # drop missing values (simple for now)
    df = df.dropna()

    # STANDARDIZE column names (IMPORTANT FIX)
    df.columns = df.columns.str.strip().str.lower()

    # ensure churn is numeric
    if "churn" in df.columns:
        df["churn"] = df["churn"].astype(int)

    print(f"[INFO] Cleaned data shape: {df.shape}")
    print(f"[DEBUG] Columns: {df.columns}")

    return df