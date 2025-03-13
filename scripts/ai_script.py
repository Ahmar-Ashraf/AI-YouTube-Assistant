import openai

openai.api_key = "YOUR_OPENAI_API_KEY"

def generate_script(topic):
    prompt = f"Write a YouTube video script about {topic}."
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

topic = "Top 10 AI Tools"
print(generate_script(topic))