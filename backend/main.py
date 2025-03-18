from flask import Flask, request, jsonify
from stu import StuTheStork  # Import your StuTheStork class from stu.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    # Get user input from the incoming request
    data = request.json
    user_input = data.get("question", "")
    
    # Create an instance of StuTheStork
    stu = StuTheStork()
    
    # Get the response (either predefined or GPT-2 generated)
    response = stu.match_question(user_input)
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
