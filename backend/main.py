from flask import Flask, request, jsonify
from backend.stu import StuTheStork  # <-- Import the Stu class here
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    stu = StuTheStork()  # Create an instance of StuTheStork
    response = stu.match_question(user_input)  # Call match_question method
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)

