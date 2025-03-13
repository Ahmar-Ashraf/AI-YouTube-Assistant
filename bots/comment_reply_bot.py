from googleapiclient.discovery import build
import openai

api_key = "YOUR_YOUTUBE_API_KEY"
channel_id = "YOUR_CHANNEL_ID"
openai.api_key = "YOUR_OPENAI_API_KEY"

youtube = build("youtube", "v3", developerKey=api_key)

def get_latest_comment(video_id):
    request = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        order="time",
        maxResults=1
    )
    response = request.execute()
    
    comment = response["items"][0]["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
    comment_id = response["items"][0]["id"]
    
    return comment, comment_id

def generate_ai_reply(comment_text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": f"Reply to this YouTube comment: {comment_text}"}]
    )
    return response["choices"][0]["message"]["content"]

def post_reply(video_id):
    comment_text, comment_id = get_latest_comment(video_id)
    reply_text = generate_ai_reply(comment_text)
    
    request = youtube.comments().insert(
        part="snippet",
        body={
            "snippet": {
                "parentId": comment_id,
                "textOriginal": reply_text
            }
        }
    )
    request.execute()
    print("Replied to comment:", comment_text)

video_id = "YOUR_VIDEO_ID"
post_reply(video_id)