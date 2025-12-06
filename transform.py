def transform_series(df):

    # Normaliza gênero
    df["genre"] = df["genre"].str.lower()

    # Duração média por gênero
    durations = {
        "crime": 47,
        "adventure": 24,
        "sci-fi": 50,
        "comedy": 22
    }
    
    df["avg_episode_duration"] = df["genre"].map(durations)

    # Popularidade
    weights = {
        "crime": 4,
        "adventure": 3,
        "sci-fi": 4,
        "comedy": 2
    }

    df["popularity_score"] = df["episodes"] * df["genre"].map(weights)

    return df