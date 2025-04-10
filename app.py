from flask import Flask, request, jsonify
import google.generativeai as genai

app = Flask(__name__)

genai.configure(api_key="AIzaSyDViD3nOqtAUr7eLQ5nP1f3BqJ3diLOaZI")

model = genai.GenerativeModel("gemini-pro")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]
    response = model.generate_content(user_input)
    return jsonify({"reply": response.text})

if __name__ == "__main__":
    app.run()
