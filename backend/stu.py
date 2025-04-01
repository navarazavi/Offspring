import random
import re

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
                # Add more advanced fertility-related questions here...
                {"question": "What is polycystic ovary syndrome (PCOS)?", 
                 "answer": "PCOS is a common hormonal disorder that can affect ovulation and fertility. It can cause irregular periods, high levels of androgens (male hormones), and cysts on the ovaries."},
    
                {"question": "How does age affect fertility?", 
                 "answer": "Fertility naturally declines with age, particularly for women. Women's egg quantity and quality decrease with age, and men may experience reduced sperm quality after age 40."},
    
                {"question": "What are fallopian tube blockages and how do they affect fertility?", 
                 "answer": "Blockages in the fallopian tubes prevent the egg from meeting the sperm, which can lead to infertility. Causes may include infections, pelvic inflammatory disease (PID), or endometriosis."},
    
                {"question": "What is endometriosis?", 
                 "answer": "Endometriosis occurs when tissue similar to the uterine lining grows outside the uterus. It can cause pain, scarring, and infertility by affecting the ovaries, fallopian tubes, and pelvic tissue."},
    
                {"question": "What is the role of luteal phase defect in fertility?", 
                 "answer": "A luteal phase defect occurs when the second half of the menstrual cycle (the luteal phase) is shorter than normal, which can prevent implantation of a fertilized egg."},
    
                {"question": "Can stress affect fertility?", 
                 "answer": "Yes, high stress can interfere with hormone regulation, affecting ovulation and sperm production. Reducing stress through relaxation techniques can improve fertility."},
    
                {"question": "What is sperm motility?", 
                 "answer": "Sperm motility refers to the sperm's ability to move efficiently. Poor motility can decrease the chances of sperm reaching the egg, affecting fertility."},
    
                {"question": "What are the signs of low testosterone in men?", 
                 "answer": "Signs of low testosterone in men include low energy, reduced libido, erectile dysfunction, and infertility. Treatment options may involve hormone therapy."},
    
                {"question": "What is intrauterine insemination (IUI)?", 
                 "answer": "IUI is a fertility treatment where sperm is directly injected into the uterus to increase the chances of fertilization, often used in cases of mild male infertility or unexplained infertility."},
    
                {"question": "How does body weight affect fertility?", 
                 "answer": "Both low and high body weight can affect fertility. Extreme weight fluctuations can interfere with ovulation and sperm production. Maintaining a healthy weight is key for fertility."},
    
                {"question": "What is the impact of alcohol on fertility?", 
                 "answer": "Heavy alcohol consumption can interfere with hormone production, ovulation, and sperm health. It's recommended to limit alcohol intake when trying to conceive."},
    
                {"question": "What is egg freezing?", 
                 "answer": "Egg freezing is the process of preserving a woman’s eggs for future use, often used for women who want to delay childbearing due to medical or personal reasons."},
    
                {"question": "What are uterine fibroids and how do they affect fertility?", 
                 "answer": "Uterine fibroids are benign tumors in the uterus that can interfere with implantation, cause miscarriage, or obstruct the fallopian tubes, impacting fertility."},
    
                {"question": "What is a chemical pregnancy?", 
                 "answer": "A chemical pregnancy occurs when an embryo is fertilized but does not implant properly, often leading to a very early miscarriage that might go unnoticed."},
    
                {"question": "How can I track my ovulation?", 
                 "answer": "You can track ovulation through methods like tracking your menstrual cycle, using ovulation predictor kits (OPKs), basal body temperature, and cervical mucus monitoring."},
    
                {"question": "What is sperm count and how does it affect fertility?", 
                 "answer": "Sperm count refers to the concentration of sperm in a man’s semen. Low sperm count can affect fertility by reducing the chances of the sperm reaching and fertilizing an egg."}
            ]
        }
        
        # Store user context, if any
        self.user_context = {}

    def match_question(self, user_input):
        """Match user input to a known question and return an appropriate response."""
        user_input_lower = user_input.lower()

        # Enhanced matching with regex and context
        if re.search(r"\b(hi|hello|hey)\b", user_input_lower):
            return random.choice(self.responses["greeting"])
        elif re.search(r"\b(struggling|broken|help|hard)\b", user_input_lower):
            return random.choice(self.responses["encouragement"])
        elif re.search(r"\b(cycle|ovulation|fertile|window|period)\b", user_input_lower):
            return random.choice(self.responses["cycle_tracking"])
        elif re.search(r"\b(doctor|consult|specialist)\b", user_input_lower):
            return random.choice(self.responses["consultation"])
        elif re.search(r"\b(joke|funny|laugh|humor)\b", user_input_lower):
            return random.choice(self.responses["funny"])

        # Check if user wants to know Stu's favorite song
        if "favorite song" in user_input_lower:
            return "Stu's favorite song? It's 'Once in a Lifetime' by Talking Heads! A classic! 🎶"

        # Add Stu's zodiac sign response
        if "zodiac" in user_input_lower or "sign" in user_input_lower:
            return "I'm a triple Pisces. Do you have a box of tissues? I'm getting emotional 😢"

        # Contextual responses - use previously collected data if available
        if "name" in user_input_lower:
            if "name" not in self.user_context:
                self.user_context["name"] = user_input.split()[-1]  # Assuming the name is at the end of the sentence
                return f"Nice to meet you, {self.user_context['name']}! How can I assist you with your fertility journey today?"
            else:
                return f"Hey again, {self.user_context['name']}! How can I help today?"

        # Check if it matches any specific fertility-related questions
        for response in self.responses["general_fertility_questions"]:
            if re.search(response["question"].lower(), user_input_lower):
                return response["answer"]

        # Default response if no match found
        return "I’m not sure about that, but I’m here to help with fertility insights. Let’s track your journey together!"

