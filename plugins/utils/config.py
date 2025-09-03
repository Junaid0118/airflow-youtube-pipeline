import os

DB_CONFIG = {
    "USER": os.getenv("DB_USER", "dev"),
    "PASSWORD": os.getenv("DB_PASSWORD", ""),
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": os.getenv("DB_PORT", "5432"),
    "NAME": os.getenv("DB_NAME", "airflow_youtube"),
}
