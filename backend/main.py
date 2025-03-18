import sys
import os

# Add the current directory to sys.path to ensure Python can find 'stu.py'
sys.path.append(os.path.abspath(os.path.dirname(__file__)))

from flask import Flask, request, jsonify
from stu import ask_stu  # Importing the function directly from stu.py
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # This enables CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu_route():
    # Get user input from the incoming request
    data = request.json
    user_input = data.get("question", "")
    
    # Get the response from the simplified ask_stu function
    response = ask_stu(user_input)  # Call the simpler ask_stu function
    
    # Return the response as JSON
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)


