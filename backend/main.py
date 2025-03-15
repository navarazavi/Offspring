from flask import Flask, request, jsonify
from stu import stu_chatbot

app = Flask(__name__)

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    response = stu_chatbot(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
