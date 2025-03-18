from flask import Flask, request, jsonify
from backend.stu import StuTheStork  # <-- Import the Stu class here
import openai
import os

# Load the OpenAI API key from environment variables (Render)
openai_api_key = os.getenv('OPENAI_API_KEY')

# Set OpenAI API key
openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    
    stu = StuTheStork()  # Create an instance of StuTheStork
    
    # First, check if Stu can handle the question directly
    response = stu.match_question(user_input)
    
    # If Stu can't answer, try using GPT-4 for a more detailed response
    if response == "I'm still learning! Try asking about fertility tracking, cycles, or consultations.":
        # If the response is the default one, query GPT-4
        gpt_response = openai.chat_completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        response = gpt_response['choices'][0]['message']['content'].strip()
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
