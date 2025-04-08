import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("YOUTUBE_API_KEY")

def search_product_videos(product_name, max_results=5):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": f"{product_name} review OR unboxing",
        "type": "video",
        "maxResults": max_results,
        "videoDuration": "short",
        "key": API_KEY
    }

    response = requests.get(url, params=params)
    data = response.json()

    results = []
    for item in data.get("items", []):
        video_id = item["id"]["videoId"]
        title = item["snippet"]["title"]
        channel = item["snippet"]["channelTitle"]
        thumbnail = item["snippet"]["thumbnails"]["medium"]["url"]
        url = f"https://www.youtube.com/watch?v={video_id}"

        results.append({
            "title": title,
            "channel": channel,
            "video_id": video_id,
            "url": url,
            "thumbnail": thumbnail
        })

    return results

# 🔽 Test block (safe to include at the bottom while developing)
if __name__ == "__main__":
    test_query = "Neutrogena sunscreen"
    videos = search_product_videos(test_query, max_results=3)

    print(f"\n🔍 YouTube Results for '{test_query}':\n")
    for v in videos:
        print(f"📹 {v['title']}")
        print(f"🔗 {v['url']}")
        print(f"🧠 Channel: {v['channel']}")
        print("---")
