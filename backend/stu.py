ffrom flask import Flask, request, jsonify
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
                {"question": "How do I know when I'm most fertile?", "answer": "The most fertile time is typically during ovulation, which occurs around 14 days before your next period."},
                # Add more general fertility questions here
            ]
        }

    def get_response(self, category):
        """Returns a response based on the requested category."""
        return random.choice(self.responses.get(category, ["I'm not sure how to help with that, but let's track what we can!"]))

# Function to integrate with main.py
@app.route('/ask_stu', methods=['POST'])
def stu_chatbot():
    user_input = request.json.get('question')  # <-- Extract user input from the request
    
    stu = StuTheStork()

    # General matching approach (loosely checking for any relevant words)
    if "hello" in user_input.lower() or "hi" in user_input.lower():
        return jsonify({"response": stu.get_response("greeting")})
    elif "help" in user_input.lower() or "struggling" in user_input.lower():
        return jsonify({"response": stu.get_response("encouragement")})
    elif "cycle" in user_input.lower() or "ovulation" in user_input.lower():
        return jsonify({"response": stu.get_response("cycle_tracking")})
    elif "doctor" in user_input.lower() or "consult" in user_input.lower():
        return jsonify({"response": stu.get_response("consultation")})
    
    # Match general fertility questions
    for response in stu.responses["general_fertility_questions"]:
        if any(word in user_input.lower() for word in response["question"].lower().split()):
            return jsonify({"response": response["answer"]})
    
    return jsonify({"response": "I'm still learning! Try asking about fertility tracking, cycles, or consultations."})

if __name__ == '__main__':
    app.run(debug=True)
