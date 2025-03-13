from googleapiclient.discovery import build

api_key = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

def get_video_performance(video_id):
    request = youtube.videos().list(
        part="statistics",
        id=video_id
    )
    response = request.execute()
    return response["items"][0]["statistics"]

video_id = "YOUR_VIDEO_ID"
stats = get_video_performance(video_id)
print(f"Views: {stats['viewCount']}, Likes: {stats['likeCount']}, Comments: {stats['commentCount']}")