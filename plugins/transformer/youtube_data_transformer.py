from typing import Dict

class YouTubeDataTransformer:

    @staticmethod
    def transform(video: Dict) -> Dict:
        snippet = video.get("snippet", {})
        statistics = video.get("statistics", {})
        return {
            "video_id": video.get("id"),
            "title": snippet.get("title"),
            "channel_title": snippet.get("channelTitle"),
            "view_count": statistics.get("viewCount"),
            "like_count": statistics.get("likeCount"),
            "comment_count": statistics.get("commentCount"),
        }
