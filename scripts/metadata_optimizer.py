import openai  

openai.api_key = "YOUR_OPENAI_API_KEY"  

def optimize_metadata(title, description):  
    prompt = f"Optimize this YouTube title and description for SEO:\nTitle: {title}\nDescription: {description}"  
    response = openai.ChatCompletion.create(  
        model="gpt-4",  
        messages=[{"role": "user", "content": prompt}]  
    )  
    return response["choices"][0]["message"]["content"]  

title = "AI Tools for Beginners"  
description = "Learn about the best AI tools in 2025 that can help beginners get started."  
print(optimize_metadata(title, description))