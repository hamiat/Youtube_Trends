import pandas as pd
from config import fetch_data

def process_items(items):
    rows = [
        {
            "video_id": item.get("id", ""),
            "title": item.get("snippet", {}).get("title", ""),
            "channel": item.get("snippet", {}).get("channelTitle", ""),
            "category_id": item.get("snippet", {}).get("categoryId", ""),
            "publish_time": item.get("snippet", {}).get("publishedAt", ""),
            "tags": ", ".join(item.get("snippet", {}).get("tags", [])),
            "duration": item.get("contentDetails", {}).get("duration", ""),
            "view_count": int(item.get("statistics", {}).get("viewCount", 0)),
            "like_count": int(item.get("statistics", {}).get("likeCount", 0)),
            "comment_count": int(item.get("statistics", {}).get("commentCount", 0)),
            "paid_ads" : item.get("paidProductPlacementDetails", {}).get("hasPaidProductPlacement", ""),
            "region" : item.get("code", "")
        }
        for item in items
    ]

    df = pd.DataFrame(rows)
    print(df)
    return df
    
def create_dataset():
    items = fetch_data()
    df = process_items(items)
    df.to_csv("trending_videos.csv", index = False)


if __name__ == "__main__":
    create_dataset()