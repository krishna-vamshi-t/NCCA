import os
from src.utils import generate_all_assets
from src.config import DATA_PATH
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import create_features
from src.segmentation import segment_customers, churn_by_segment
from src.metrics import (
    churn_rate,
    churn_by_column,
    high_risk_percentage,
    engagement_vs_churn
)


def run_pipeline(mode="full"):
    print("\nPIPELINE STARTED\n")

    # Step 1: Load data
    df = load_data(DATA_PATH)
    print("[INFO] Loaded data shape:", df.shape)

    # Step 2: Clean data
    df_clean = clean_data(df)
    print("[INFO] Cleaned data shape:", df_clean.shape)

    # Step 3: Lowercase all column names
    df_clean.columns = df_clean.columns.str.lower()

    # Step 4: Feature engineering
    df_final = create_features(df_clean)
    print("[INFO] Feature engineering completed:", df_final.shape)

    # Step 5: Segmentation
    if mode == "full":
        df_final = segment_customers(df_final)
        churn_by_segment(df_final)

    # Step 6: Metrics
    churn_rate(df_final)
    churn_by_column(df_final, "subscriptionplan")
    churn_by_column(df_final, "country")
    high_risk_percentage(df_final)
    engagement_vs_churn(df_final)

    # Step 7: Export processed data for Power BI
    os.makedirs("data/processed", exist_ok=True)
    df_final.to_csv("data/processed/netflix_processed.csv", index=False)
    print("[INFO] Exported processed data to data/processed/netflix_processed.csv")

    # Step 8: Generate assets
    generate_all_assets(df_final)

    print("\nPIPELINE COMPLETED SUCCESSFULLY\n")


if __name__ == "__main__":
    run_pipeline()