from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Added for CORS support
from backend.stu import stu_chatbot

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    response = stu_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

