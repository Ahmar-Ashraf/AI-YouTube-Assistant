from googleapiclient.discovery import build  

api_key = "YOUR_YOUTUBE_API_KEY"  
youtube = build("youtube", "v3", developerKey=api_key)  

def get_trending_videos(region="US"):  
    request = youtube.videos().list(  
        part="snippet",  
        chart="mostPopular",  
        regionCode=region,  
        maxResults=5  
    )  
    response = request.execute()  

    for item in response["items"]:  
        print(f"Title: {item['snippet']['title']}\nURL: https://www.youtube.com/watch?v={item['id']}\n")  

get_trending_videos()