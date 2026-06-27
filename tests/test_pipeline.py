import pandas as pd
import pytest
from src.data_loader import load_data
from src.data_cleaning import clean_data
from src.feature_engineering import create_features
from src.segmentation import segment_customers

DATA_PATH = "data/raw/netflix_customer_churn_dataset.csv"


def test_data_loads():
    df = load_data(DATA_PATH)
    assert df is not None
    assert len(df) > 0
    print("data loads fine")


def test_no_nulls_after_cleaning():
    df = load_data(DATA_PATH)
    df_clean = clean_data(df)
    df_clean.columns = df_clean.columns.str.lower()
    assert df_clean.isnull().sum().sum() == 0
    print("no nulls after cleaning")


def test_feature_columns_exist():
    df = load_data(DATA_PATH)
    df_clean = clean_data(df)
    df_clean.columns = df_clean.columns.str.lower()
    df_final = create_features(df_clean)
    assert "engagement_score" in df_final.columns
    assert "tenure_group" in df_final.columns
    assert "activity_level" in df_final.columns
    assert "payment_risk" in df_final.columns
    print("all feature columns exist")


def test_churn_column_is_binary():
    df = load_data(DATA_PATH)
    df_clean = clean_data(df)
    df_clean.columns = df_clean.columns.str.lower()
    assert set(df_clean["churn"].unique()).issubset({0, 1})
    print("churn column is binary")


def test_segments_assigned():
    df = load_data(DATA_PATH)
    df_clean = clean_data(df)
    df_clean.columns = df_clean.columns.str.lower()
    df_final = create_features(df_clean)
    df_final = segment_customers(df_final)
    assert "segment" in df_final.columns
    assert df_final["segment"].isnull().sum() == 0
    print("segments assigned to all customers")


def test_cleaned_data_smaller_than_raw():
    df = load_data(DATA_PATH)
    df_clean = clean_data(df)
    assert len(df_clean) < len(df)
    print("cleaning removed rows as expected")