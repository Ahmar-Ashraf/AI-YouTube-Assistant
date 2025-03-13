from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

api_key = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "My AI-Generated Video",
            "description": "This video was created by AI!",
            "tags": ["AI", "automation", "YouTube"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload("final_video.mp4")
)

response = request.execute()
print(response)from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

api_key = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

# Use the video from static/videos/
video_path = "static/videos/final_video.mp4"

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "My AI-Generated Video",
            "description": "This video was created by AI!",
            "tags": ["AI", "automation", "YouTube"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload(video_path)
)

response = request.execute()
print(response)from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

api_key = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.videos().insert(
    part="snippet,status",
    body={
        "snippet": {
            "title": "My AI-Generated Video",
            "description": "This video was created by AI!",
            "tags": ["AI", "automation", "YouTube"],
            "categoryId": "22"
        },
        "status": {"privacyStatus": "public"}
    },
    media_body=MediaFileUpload("final_video.mp4")
)

response = request.execute()
print(response)