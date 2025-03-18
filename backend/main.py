from flask import Flask, request, jsonify
from flask_cors import CORS
from stu import StuTheStork  # Make sure stu.py is in the same folder or import path

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json  # Get the user input (question)
    user_input = data.get("question", "")
    
    stu = StuTheStork()
    response = stu.match_question(user_input)  # Use the matching function to get a response
    
    return jsonify({"response": response})  # Return the response in JSON format

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
