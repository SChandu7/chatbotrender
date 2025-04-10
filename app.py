


from flask import Flask, request, jsonify
import google.generativeai as genai
import os

app = Flask(__name__)

# Set your Gemini API key here
genai.configure(api_key=os.getenv("AIzaSyDViD3nOqtAUr7eLQ5nP1f3BqJ3diLOaZI"))

model = genai.GenerativeModel('gemini-pro')

@app.route('/')
def home():
    return "Gemini Chatbot API is running!"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_message = data.get('message', '')

    try:
        response = model.generate_content(user_message)
        return jsonify({'reply': response.text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

