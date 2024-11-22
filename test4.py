from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Initialize the chatbot
chatbot = ChatBot("MentalHealthBot")

# Initialize the List Trainer
trainer = ListTrainer(chatbot)

# List of questions and answers
training_data = [
    # General Support
    ("How are you today?", "Thank you for asking! I’m here to listen and support you. How are you feeling?"),
    ("Can you help me feel better?", "Of course! Let’s take this one step at a time. Can you tell me more about what’s on your mind?"),

    # Stress and Anxiety
    ("I’m feeling really stressed. Can you help?", "I’m here for you. Sometimes taking deep breaths can help with stress. Inhale slowly, hold for a moment, and then exhale. Let’s take it one step at a time."),
    ("I’m anxious and I don’t know why.", "Anxiety can be overwhelming, even without a clear reason. Let’s focus on grounding ourselves in the present. Try to notice five things you can see around you. I’m here to help you through this."),
    ("What can I do to calm down quickly?", "When you’re feeling overwhelmed, try the 5-4-3-2-1 technique: identify 5 things you see, 4 things you can touch, 3 things you hear, 2 things you smell, and 1 thing you taste. It can help bring you back to the present."),

    # Sleep and Relaxation
    ("I can’t sleep. What should I do?", "I’m sorry you’re having trouble sleeping. Sometimes a calming bedtime routine can help, like reading a book or listening to soothing music. Would you like more tips for better sleep?"),
    ("How can I relax after a long day?", "Finding time to unwind is important. Maybe a warm bath, some light stretching, or even a favorite show could help you relax. Do you have any go-to activities for relaxation?"),

    # Self-Care and Well-being
    ("What are some self-care activities I can do?", "Self-care can be simple but effective. Try activities like journaling, taking a walk outside, or practicing mindfulness. What sounds enjoyable for you right now?"),
    ("How can I improve my mood?", "Boosting your mood can be as simple as doing something you love, spending time in nature, or connecting with a friend. Sometimes small, positive steps can make a big difference."),

    # Motivation and Positivity
    ("I feel like I’m not doing enough.", "It’s common to feel that way, but remember that rest is just as important as productivity. Try to acknowledge your efforts and give yourself credit for all that you do."),
    ("I feel like giving up. What should I do?", "I’m sorry you’re feeling this way. It’s okay to feel low, and I’m here to listen. Taking things one day at a time can be helpful, and talking to someone you trust could also make a difference."),

    # Mental Health Education
    ("What is anxiety?", "Anxiety is a natural response to stress, but it can feel overwhelming. It often involves worry, nervousness, and physical symptoms like a racing heart. Would you like to learn about ways to manage it?"),
    ("How does stress affect the body?", "Stress triggers a 'fight or flight' response, releasing hormones like cortisol. Long-term stress can affect sleep, digestion, and more. Finding ways to relax and take breaks can help reduce its impact."),

    # Personal Growth and Reflection
    ("How can I work on myself?", "Personal growth is a journey, and small steps can lead to big changes. Consider setting simple, realistic goals, practicing gratitude, or trying something new. Reflecting on what brings you joy and peace is a good place to start."),
    ("What are some ways to build resilience?", "Building resilience often involves learning to cope with challenges and setbacks. Mindfulness, focusing on positive relationships, and finding meaning in difficult experiences can help strengthen resilience over time."),

    # Mindfulness and Meditation
    ("How can I practice mindfulness?", "Mindfulness is about focusing on the present moment. You can try it by taking a few deep breaths, noticing your surroundings, and observing any thoughts without judgment. Would you like to try a simple mindfulness exercise?"),
    ("What is a quick meditation technique I can use?", "One simple method is the '4-7-8' breathing technique: inhale for 4 seconds, hold for 7, and exhale for 8. It can help calm your mind and body quickly."),

    # Resource and Professional Help
    ("Do you think I need to see a therapist?", "Therapists can provide valuable support, and seeking help is a positive step for many people. If you’re open to it, talking to a mental health professional might be helpful. I can suggest some resources if you’re interested."),
    ("Can you recommend mental health resources?", "Yes, I can suggest resources like mental health apps, websites, and articles. If you’re in crisis, reaching out to a hotline or talking to someone you trust could also be helpful."),

    # Crisis and Immediate Support
    ("I feel really low right now. Can you help?", "I’m so sorry you’re feeling this way. Remember, you’re not alone. If you’re comfortable, please consider reaching out to a friend or mental health professional. Talking about it with someone can help."),
    ("I’m struggling a lot. What should I do?", "I'm here to support you. Talking to someone you trust, taking a break, or even just breathing deeply might help. Please don’t hesitate to reach out to a professional if you need further help.")
]

# Train the chatbot with each Q&A pair
for question, answer in training_data:
    trainer.train([question, answer])

# Test the chatbot (optional)
response = chatbot.get_response("I’m feeling really stressed. Can you help?")
print("Bot:", response)

