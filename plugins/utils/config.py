import os

CONFIG = {
    "USER": os.getenv("DB_USER", "dev"),
    "PASSWORD": os.getenv("DB_PASSWORD", ""),
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", "5432"),
    "NAME": os.getenv("DB_NAME", "airflow_youtube"),
    "API_KEY": os.getenv("YT_API_KEY", ""),
    "API_URL": "https://www.googleapis.com/youtube/v3/videos",
    "REGION_CODE": "US",
    "MAX_RESULTS": 50,
    "OUTPUT_FILE": "youtube_trending.csv"
}
