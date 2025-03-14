import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "AI YouTube Assistant is running!"

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is missing
    app.run(host='0.0.0.0', port=port)