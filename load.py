import sqlite3

def load_to_sqlite(df, db_path="series.db"):
    conn = sqlite3.connect(db_path)
    df.to_sql("tv_shows", conn, if_exists="replace", index=False)
    conn.close()