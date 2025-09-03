from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from plugins.utils.config import CONFIG
from plugins.utils.base import Base  

DB_URL = f"postgresql+psycopg2://{CONFIG['USER']}:{CONFIG['PASSWORD']}@{CONFIG['HOST']}:{CONFIG['PORT']}/{CONFIG['NAME']}"
engine = create_engine(DB_URL, echo=True, pool_pre_ping=True)
SessionLocal = sessionmaker(bind=engine)

def get_session():
    return SessionLocal()

def init_db():
    from plugins.models.youtube_trending import YouTubeTrending
    Base.metadata.create_all(bind=engine)
    print("✅ Tables created successfully!")
