from googleapiclient.discovery import build
import time

api_key = "YOUR_YOUTUBE_API_KEY"
video_id = "YOUR_VIDEO_ID"

youtube = build("youtube", "v3", developerKey=api_key)

def get_video_statistics(video_id):
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()
    return response["items"][0]["statistics"]

def monitor_video(video_id, interval=60):
    print(f"Monitoring video: {video_id}")
    last_stats = get_video_statistics(video_id)

    while True:
        time.sleep(interval)
        new_stats = get_video_statistics(video_id)

        if new_stats["viewCount"] != last_stats["viewCount"]:
            print(f"Views changed: {last_stats['viewCount']} → {new_stats['viewCount']}")
        
        if new_stats["likeCount"] != last_stats["likeCount"]:
            print(f"Likes changed: {last_stats['likeCount']} → {new_stats['likeCount']}")

        last_stats = new_stats

monitor_video(video_id)