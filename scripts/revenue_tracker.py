from googleapiclient.discovery import build  

api_key = "YOUR_YOUTUBE_API_KEY"  
youtube = build("youtube", "v3", developerKey=api_key)  

def get_channel_earnings(channel_id):  
    request = youtube.channels().list(  
        part="statistics",  
        id=channel_id  
    )  
    response = request.execute()  

    stats = response["items"][0]["statistics"]  
    print(f"Subscribers: {stats['subscriberCount']}")  
    print(f"Total Views: {stats['viewCount']}")  

channel_id = "YOUR_CHANNEL_ID"  
get_channel_earnings(channel_id)