from googleapiclient.discovery import build

api_key = "YOUR_YOUTUBE_API_KEY"
youtube = build("youtube", "v3", developerKey=api_key)

request = youtube.channels().list(
    part="statistics",
    id="UC_x5XG1OV2P6uZZ5FSM9Ttw"  # Replace with your channel ID
)
response = request.execute()

print(response)