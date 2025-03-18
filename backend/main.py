from flask import Flask, request, jsonify
from flask_cors import CORS  # <-- Added for CORS support
from backend.stu import StuTheStork  # <-- Correct import for the class

app = Flask(__name__)
CORS(app)  # <-- This enables CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    
    # Instantiate the StuTheStork class
    stu = StuTheStork()
    
    # Get the response based on the user input
    response = stu.get_response(user_input)  # Use the get_response method
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
