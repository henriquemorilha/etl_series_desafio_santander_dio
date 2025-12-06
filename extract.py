import pandas as pd

def extract_series(path: str):
    return pd.read_csv(path)