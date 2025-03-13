import openai  

openai.api_key = "YOUR_OPENAI_API_KEY"  

def generate_hashtags(topic):  
    prompt = f"Generate trending YouTube hashtags for a video about {topic}."  
    response = openai.ChatCompletion.create(  
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}]  
    )  
    return response["choices"][0]["message"]["content"]  

topic = "AI in 2025"  
print(generate_hashtags(topic))