from flask import Flask, request, jsonify
import random

app = Flask(__name__)

class StuTheStork:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hey there! I'm Stu the Stork, here to help with fertility insights.",
                "Hello! How can I support your fertility journey today?",
                "Hi, I'm Stu. Let's talk fertility tracking!"
            ],
            "encouragement": [
                "I know this journey can be hard, but you're doing your best. 💙",
                "You're not broken—fertility is complex, and I'm here to help track what we can.",
                "Small changes can make a big impact. Let’s look at your data together."
            ],
            "cycle_tracking": [
                "Based on your Apple Health data, your predicted fertility window starts soon.",
                "Tracking temperature trends can help pinpoint ovulation. Want to log today’s data?",
                "Have you considered syncing your cycle with your partner’s Apple Health for joint tracking?"
            ],
            "consultation": [
                "I'm here to provide insights, but a fertility specialist can give personalized advice.",
                "I can help track trends, but a doctor can run the right tests to dig deeper.",
                "It might be helpful to consult an expert for more guidance. I can help track symptoms in the meantime."
            ],
            "general_fertility_questions": [
                {"question": "What is fertility?", "answer": "Fertility is the natural ability to conceive a child, involving the functioning of the reproductive system."},
                # Add more questions and answers here
            ]
        }

    def get_response(self, category):
        """Returns a response based on the requested category."""
        return random.choice(self.responses.get(category, ["I'm not sure how to help with that, but let's track what we can!"]))

    def match_question(self, user_input):
        """Match user input to a known question."""
        print(f"Received user input: {user_input}")  # Log the user input for debugging
        
        if any(word in user_input.lower() for word in ["hi", "hello", "hey"]):
            return "greeting"
        elif any(word in user_input.lower() for word in ["struggling", "broken", "help", "hard"]):
            return "encouragement"
        elif any(word in user_input.lower() for word in ["cycle", "ovulation", "fertile", "window"]):
            return "cycle_tracking"
        elif any(word in user_input.lower() for word in ["doctor", "consult", "specialist"]):
            return "consultation"
        
        for response in self.responses["general_fertility_questions"]:
            if any(word in user_input.lower() for word in response["question"].lower().split()):
                return response["answer"]
        
        return "I'm still learning! Try asking about fertility tracking, cycles, or consultations."

# Function to integrate with main.py
@app.route('/ask_stu', methods=['POST'])
def stu_chatbot():
    user_input = request.json.get('question')  # <-- Extract user input from the request
    stu = StuTheStork()
    
    # Log input for debugging
    print(f"User input received: {user_input}")
    
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
    app.run(debug=True)
