import pandas as pd
import streamlit as st
from config import fetch_data

def process_data():
    rows= []
    items = fetch_data()

    for item in items:
        snippet = item.get("snippet", {})
        stats = item.get("statistics", {})
        video_id = item.get("id", "")

        try: 
            rows.append({
                "video_id": video_id,
                "title": snippet.get("title", ""),
                "channel": snippet.get("channelTitle", ""),
                "category_id": snippet.get("categoryId", ""),
                "publish_time": snippet.get("publishedAt", ""),
                "view_count": int(stats.get("viewCount", 0)),
                "like_count": int(stats.get("likeCount", 0)),
                "comment_count": int(stats.get("commentCount", 0))})
        except Exception as e:
            print(f"Skipping video due to error: {e}")
    
    df = pd.DataFrame(rows)
    return df

def create_dataset():
    df = process_data()
    df.to_csv("trending_videos.csv", index = False)


if __name__ == "__main__":
    create_dataset()