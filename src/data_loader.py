import pandas as pd
import os

def load_data(path: str) -> pd.DataFrame:
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found: {path}")

    df = pd.read_csv(path)

    if df.empty:
        raise ValueError("Dataset is empty")

    print(f"[INFO] Loaded data shape: {df.shape}")

    return df