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

    # Find the category or get a general response
    category_or_response = stu.match_question(user_input)
    
    # If it's a category, get a response based on that
    if isinstance(category_or_response, str) and category_or_response in stu.responses:
        response = stu.get_response(category_or_response)
    else:
        # Otherwise, we have a general response (a direct answer)
        response = category_or_response
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
