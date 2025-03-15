import random

class StuTheStork:
    def __init__(self):
        self.responses = {
            "greeting": [
                "Hey there! I'm Stu the Stork, here to help with fertility insights.",
                "Hello! How can I support your fertility journey today?",
                "Hi, I'm Stu. Let's talk fertility tracking!"
            ],
            "encouragement": [
                "I know this journey can be hard, but you're doing your best.",
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
            ]
        }

    def get_response(self, category):
        """Returns a response based on the requested category."""
        return random.choice(self.responses.get(category, ["I'm not sure how to help with that, but let's track what we can!"]))

# Function to integrate with main.py
def stu_chatbot(user_input):
    """Maps user input to predefined categories."""
    stu = StuTheStork()

    # Basic keyword matching
    if any(word in user_input.lower() for word in ["hi", "hello", "hey"]):
        return stu.get_response("greeting")
    elif any(word in user_input.lower() for word in ["struggling", "broken", "help", "hard"]):
        return stu.get_response("encouragement")
    elif any(word in user_input.lower() for word in ["cycle", "ovulation", "fertile", "window"]):
        return stu.get_response("cycle_tracking")
    elif any(word in user_input.lower() for word in ["doctor", "consult", "specialist"]):
        return stu.get_response("consultation")
    
    return "I'm still learning! Try asking about fertility tracking, cycles, or consultations."

