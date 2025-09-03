from sqlalchemy import Column, Integer, String, BigInteger, Float
from plugins.utils.db import Base

class YouTubeTrending(Base):
    __tablename__ = "youtube_trending"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    video_id = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    channel_title = Column(String, nullable=False)
    view_count = Column(BigInteger, default=0)
    like_count = Column(BigInteger, default=0)
    engagement_rate = Column(Float, default=0.0)
