from googleapiclient.discovery import build  
import openai  

openai.api_key = "YOUR_OPENAI_API_KEY"  
api_key = "YOUR_YOUTUBE_API_KEY"  

youtube = build("youtube", "v3", developerKey=api_key)  

def reply_to_comments(video_id):  
    comments_request = youtube.commentThreads().list(  
        part="snippet",  
        videoId=video_id,  
        textFormat="plainText"  
    )  
    comments_response = comments_request.execute()  

    for comment in comments_response["items"]:  
        text = comment["snippet"]["topLevelComment"]["snippet"]["textDisplay"]  
        reply = openai.ChatCompletion.create(  
            model="gpt-4",  
            messages=[{"role": "user", "content": f"Reply to this YouTube comment: {text}"}]  
        )["choices"][0]["message"]["content"]  

        youtube.comments().insert(  
            part="snippet",  
            body={  
                "snippet": {  
                    "parentId": comment["id"],  
                    "textOriginal": reply  
                }  
            }  
        ).execute()  
        print(f"Replied: {reply}")  

reply_to_comments("YOUR_VIDEO_ID")