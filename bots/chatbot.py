from flask import Flask, request, jsonify
import openai

openai.api_key = "YOUR_OPENAI_API_KEY"
app = Flask(__name__)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data["message"]

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)