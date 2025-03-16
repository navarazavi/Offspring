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
            # New category for more specific questions:
            "general_fertility_questions": [
                {"question": "What is fertility?", "answer": "Fertility is the natural ability to conceive a child, involving the functioning of the reproductive system."},
                {"question": "How do I know when I'm most fertile?", "answer": "The most fertile time is typically during ovulation, which occurs around 14 days before your next period."},
                {"question": "How can I improve my fertility?", "answer": "Maintain a healthy lifestyle with a balanced diet, exercise, stress management, and proper medical care."},
                {"question": "What is IVF?", "answer": "In vitro fertilization (IVF) is a procedure where eggs are fertilized outside the body before being implanted in the uterus."},
                {"question": "What is IUI?", "answer": "Intrauterine insemination (IUI) is a fertility treatment that involves placing sperm directly into the uterus during ovulation."},
                {"question": "What is the best age for fertility?", "answer": "Fertility peaks in the 20s and early 30s. As women age, fertility declines, especially after age 35."},
                {"question": "Can men have fertility issues?", "answer": "Yes, men can have fertility problems such as low sperm count, poor sperm motility, or low sperm quality."},
                {"question": "Can stress affect fertility?", "answer": "Yes, high stress can affect hormonal balance and ovulation, making conception more difficult."},
                {"question": "How can I track ovulation?", "answer": "You can track ovulation using basal body temperature, ovulation predictor kits, or tracking your cervical mucus."},
                {"question": "What is the cost of IVF?", "answer": "The cost of IVF varies, but it typically ranges from $12,000 to $15,000 per cycle, not including medications."},
                {"question": "How do I choose a fertility clinic?", "answer": "Research clinics with high success rates, positive patient reviews, and experienced doctors."},
                {"question": "What are the chances of IVF success?", "answer": "The success rate of IVF varies, but it generally ranges from 40% to 50% depending on age and health conditions."},
                {"question": "How can I boost my male fertility?", "answer": "Men can improve fertility by maintaining a healthy weight, reducing alcohol intake, avoiding smoking, and managing stress."},
                {"question": "Does weight affect fertility?", "answer": "Yes, being underweight or overweight can disrupt hormonal balance and affect fertility."},
                {"question": "What are common fertility treatments?", "answer": "Common treatments include medications like Clomid, IUI, IVF, and surgery for conditions like endometriosis."},
                {"question": "Is it normal to have irregular cycles?", "answer": "Irregular cycles can be common, but if they persist, it might indicate underlying health conditions such as PCOS."},
                {"question": "What is PCOS?", "answer": "Polycystic ovary syndrome (PCOS) is a hormonal disorder that affects ovulation, causing irregular periods and fertility issues."},
                {"question": "How can I find a fertility specialist?", "answer": "You can ask for referrals from your OB/GYN, or search online for reproductive endocrinologists in your area."},
                {"question": "Can age affect male fertility?", "answer": "Yes, male fertility declines with age, though it typically occurs later in life than for women."},
                {"question": "Can I get pregnant if I'm breastfeeding?", "answer": "It’s possible, though breastfeeding can suppress ovulation, making it less likely to conceive."},
                {"question": "What is egg freezing?", "answer": "Egg freezing is a process where a woman’s eggs are harvested, frozen, and stored for future use."},
                {"question": "Can fertility be restored?", "answer": "In some cases, fertility can be restored with treatments like IVF, medication, or lifestyle changes, depending on the underlying cause."},
                {"question": "What is the difference between a miscarriage and a chemical pregnancy?", "answer": "A miscarriage occurs after implantation, while a chemical pregnancy is a very early miscarriage before implantation."},
                {"question": "Does smoking affect fertility?", "answer": "Yes, smoking can harm both male and female fertility by damaging eggs and sperm and disrupting hormonal balance."},
                {"question": "How do I know if I have low sperm count?", "answer": "A semen analysis can help determine sperm count, motility, and morphology, which are key indicators of fertility."},
                {"question": "What is the role of hormones in fertility?", "answer": "Hormones like estrogen, progesterone, and testosterone regulate ovulation and sperm production, making them crucial to fertility."},
                {"question": "How does alcohol affect fertility?", "answer": "Excessive alcohol consumption can reduce fertility in both men and women by affecting hormone levels and reproductive health."},
                {"question": "How long does it take to get pregnant?", "answer": "On average, it takes about 6-12 months for a healthy couple to conceive, but it varies depending on age and health."},
                {"question": "What should I do if I'm not getting pregnant?", "answer": "If you're not getting pregnant after a year of trying, consult a fertility specialist for further evaluation."},
                {"question": "Can stress affect male fertility?", "answer": "Yes, chronic stress can lower testosterone levels and reduce sperm count and quality."},
                {"question": "Can you have children after cancer treatment?", "answer": "In many cases, fertility can be preserved through sperm banking or egg freezing before undergoing cancer treatment."},
                {"question": "What are the most common fertility issues?", "answer": "Common fertility issues include blocked fallopian tubes, PCOS, low sperm count, and endometriosis."},
                {"question": "How can I improve egg quality?", "answer": "Healthy eating, stress management, regular exercise, and supplements like CoQ10 can help improve egg quality."}
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
    
    # Matching for general fertility questions
    for response in stu.responses["general_fertility_questions"]:
        if any(word in user_input.lower() for word in response["question"].lower().split()):
            return response["answer"]
    
    return "I'm still learning! Try asking about fertility tracking, cycles, or consultations."

