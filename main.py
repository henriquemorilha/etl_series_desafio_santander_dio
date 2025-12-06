from extract import extract_series
from transform import transform_series
from load import load_to_sqlite

def run_etl():
    df = extract_series("data/series.csv")
    df_transformed = transform_series(df)
    load_to_sqlite(df_transformed)

if __name__ == "__main__":
    run_etl()