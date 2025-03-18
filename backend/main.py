from flask import Flask, request, jsonify
from backend.stu import StuTheStork  # Import the Stu class here
import openai
import os

# Load the OpenAI API key from environment variables
openai_api_key = os.getenv('OPENAI_API_KEY')

# Check if the OpenAI API key is loaded
if not openai_api_key:
    raise ValueError("The OpenAI API key is not set. Please set the OPENAI_API_KEY environment variable.")

# Set OpenAI API key
openai.api_key = openai_api_key

app = Flask(__name__)

@app.route('/ask_stu', methods=['POST'])
def ask_stu():
    data = request.json
    user_input = data.get("question", "")
    
    stu = StuTheStork()  # Create an instance of StuTheStork
    
    # Check if the user_input is empty
    if not user_input:
        return jsonify({"error": "No question provided"}), 400
    
    # First, check if Stu can handle the question directly
    response = stu.match_question(user_input)
    
    # If Stu can't answer, try using GPT-4 for a more detailed response
    if response == "I'm still learning! Try asking about fertility tracking, cycles, or consultations.":
        try:
            gpt_response = openai.Completion.create(
                model="gpt-4",  # Using GPT-4 model
                prompt=user_input,  # Directly use the user's question as the prompt
                max_tokens=150,  # Optional: limit the response length
                n=1,  # Number of responses to generate (usually 1)
                stop=None,  # Optional: specify stopping condition
                temperature=0.7  # Optional: control the randomness of the response
            )
            
            # Log the full response from GPT-4 for debugging
            print("GPT-4 Response:", gpt_response)

            response = gpt_response['choices'][0]['text'].strip()  # Access the completion text
        
        except Exception as e:
            return jsonify({"error": str(e)}), 500  # Return the error as JSON
    
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
