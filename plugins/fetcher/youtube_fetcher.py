import requests
from typing import Generator, Dict, Any
from plugins.utils.config import CONFIG as Config

class YouTubeDataFetcher:

    def __init__(self):
        self.api_key = Config['API_KEY']

    def fetch_trending_videos(self, page_token: str = None) -> Dict[str, Any]:
        params = {
            "part": "snippet,statistics",
            "chart": "mostPopular",
            "regionCode": Config['REGION_CODE'],
            "maxResults": Config['MAX_RESULTS'],
            "key": self.api_key
        }
        if page_token:
            params["pageToken"] = page_token

        response = requests.get(Config['API_URL'], params=params, timeout=10)
        response.raise_for_status()
        return response.json()

    def get_video_stream(self) -> Generator[Dict[str, Any], None, None]:
        next_page = None
        while True:
            data = self.fetch_trending_videos(next_page)
            for item in data.get("items", []):
                yield item
            next_page = data.get("nextPageToken")
            if not next_page:
                break
