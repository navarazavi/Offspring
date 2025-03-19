import random

class StuTheStork:
    def __init__(self):
        # Predefined responses
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
            "funny": [
                "Fertility can feel like a game of hide and seek... and ovulation is really good at hiding.",
                "Trying to get pregnant is like trying to win the lottery... except it takes a lot more work and there's no ticket!",
                "I’d give you advice on timing... but I’m terrible at keeping schedules, so take it with a grain of salt!"
            ],
            "general_fertility_questions": [
                {"question": "What is fertility?", "answer": "Fertility is the natural ability to conceive a child, involving the functioning of the reproductive system."},
                {"question": "How do I know when I'm most fertile?", "answer": "The most fertile time is typically during ovulation, which occurs around 14 days before your next period."},
                {"question": "How can I improve my fertility?", "answer": "Maintain a healthy lifestyle with a balanced diet, exercise, stress management, and proper medical care."},
                {"question": "What is IVF?", "answer": "In vitro fertilization (IVF) is a procedure where eggs are fertilized outside the body before being implanted in the uterus."},
                # Add more fertility-related questions here...
            ]
        }

    def match_question(self, user_input):
        """Match user input to a known question and return an appropriate response."""
        user_input_lower = user_input.lower()
        
        # Matching categories based on keywords
        if any(word in user_input_lower for word in ["hi", "hello", "hey"]):
            return random.choice(self.responses["greeting"])
        elif any(word in user_input_lower for word in ["struggling", "broken", "help", "hard"]):
            return random.choice(self.responses["encouragement"])
        elif any(word in user_input_lower for word in ["cycle", "ovulation", "fertile", "window", "period"]):
            return random.choice(self.responses["cycle_tracking"])
        elif any(word in user_input_lower for word in ["doctor", "consult", "specialist"]):
            return random.choice(self.responses["consultation"])
        elif any(word in user_input_lower for word in ["joke", "funny", "laugh", "humor"]):
            return random.choice(self.responses["funny"])

        # Add Stu's favorite song response
        if "favorite song" in user_input_lower:
            return "Stu's favorite song? It's 'Once in a Lifetime' by Talking Heads! A classic! 🎶"

        # Add Stu's zodiac sign response
        if "zodiac" in user_input_lower or "sign" in user_input_lower:
            return "I'm a triple Pisces. Do you have a box of tissues? I'm getting emotional 😢"

        # Check if it matches any specific fertility-related questions
        for response in self.responses["general_fertility_questions"]:
            if user_input_lower in response["question"].lower():
                return response["answer"]

        # Default response if no match found
        return "I’m not sure about that, but I’m here to help with fertility insights. Let’s track your journey together!"

