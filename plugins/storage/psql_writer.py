from typing import Dict, List
from sqlalchemy.orm import Session
from plugins.utils.db import SessionLocal
from plugins.models.youtube_trending import YouTubeTrending

class PostgresWriter:

    def __init__(self, batch_size: int = 1000):
        self._buffer: List[Dict] = []
        self._batch_size = batch_size

    def write(self, record: Dict):
        self._buffer.append(record)
        if len(self._buffer) >= self._batch_size:
            self.flush()

    def flush(self):
        if not self._buffer:
            return

        session: Session = SessionLocal()
        try:
            objects = [
                YouTubeTrending(
                    video_id=r.get("video_id"),
                    title=r.get("title"),
                    channel_title=r.get("channel_title"),
                    view_count=int(r.get("view_count", 0) or 0),
                    like_count=int(r.get("like_count", 0) or 0),
                )
                for r in self._buffer
            ]
            session.bulk_save_objects(objects)
            session.commit()
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()
            self._buffer.clear()

    def close(self):
        self.flush()
