print("PIPELINE STARTED")

from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import create_features
from src.metrics import (
    churn_rate,
    churn_by_column,
    high_risk_percentage,
    engagement_vs_churn
)

# Step 1: Load
df = load_data("data/netflix_customer_churn_dataset.csv")

# Step 2: Clean
df_clean = clean_data(df)

# Step 3: Feature engineering
df_final = create_features(df_clean)

# Step 4: Metrics
churn_rate(df_final)
churn_by_column(df_final, "subscriptionplan")
churn_by_column(df_final, "country")
high_risk_percentage(df_final)
engagement_vs_churn(df_final)