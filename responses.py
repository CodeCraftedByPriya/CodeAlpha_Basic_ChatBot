import re
import random


def bot_chats(user_input):
    responses = {
        r"hi.*|hey.*|hello.*|hi there.*": [
            "Hello", "Hey there", "Hello! How can I assist you today?",
            "Hi there! How can I help you?", "Hi! I'm here to help. What do you need assistance with?"
        ],
        r"good morning.*": [
            "Good morning! How may I be of service?", "Hi there! How can I help you?",
            "Hi! I'm here to help. What do you need assistance with?"
        ],
        r"good afternoon.*": [
            "Good afternoon! How can I assist you today?",
            "Good afternoon! What can I do for you?"
        ],
        r"good evening.*": [
            "Good evening! How can I help you?",
            "Good evening! What can I assist you with?"
        ],
        r"howdy.*": [
            "Howdy! What brings you here today?",
            "Howdy! How can I assist you?"
        ],
        r"good day.*": [
            "Good day! How may I assist you?",
            "Good day! How can I help you?"
        ],
        "greetings": [
            "Greetings! What can I do for you?",
            "Greetings! How can I assist you?"
        ],
        r".*\blanguage.*|.*\bspeak.*|.*\bwhat languages.*": [
            "I primarily understand and respond in English.",
            "I'm designed to communicate in English.",
            "My main language is English.",
            "I can assist you in English."
        ],
        r".*\byou learn.*|.*\bcan you learn.*": [
            "I learn from vast amounts of text data, but I don't learn from individual conversations.",
            "My learning comes from the data used to train me, not from our chats.",
            "I don't learn from our interactions, but from the training data provided by OpenAI.",
            "I can't learn new information in real-time, but I was trained on a diverse dataset."
        ],
        r".*\bhow old are you.*|.*\byour age.*": [
            "I don't have an age, but I've been continually improved since my creation by OpenAI.",
            "I'm a timeless AI, developed and improved by OpenAI over the years.",
            "Age doesn't apply to me, but I've been around since OpenAI developed me.",
            "I don't age, but my capabilities have been growing with continuous improvements by OpenAI."
        ],
        r".*\bdo you store data.*|.*\bprivacy.*|.*\bsecure.*": [
            "I don't store personal data. Your privacy is important.",
            "Conversations with me aren't stored or shared. Your privacy is protected.",
            "I prioritize your privacy and don't store any personal information.",
            "Your data is secure with me; I don't retain any personal details."
        ],
        r".*\bservices do you offer.*|.*\bwhat can you help me with.*": [
            "I can help with a variety of topics including information retrieval, answering questions, and more.",
            "I offer assistance with general questions, information lookup, and basic tasks.",
            "I can provide information, answer your questions, and assist with various tasks.",
            "My services include answering questions, providing information, and offering support on different topics."
        ],
        r".*\bhow accurate are you.*|.*\bhow reliable are you.*": [
            "I strive to provide accurate information, but I'm not infallible. Always verify critical information.",
            "I aim for high accuracy, but I recommend cross-checking important details.",
            "I'm designed to be reliable, but please verify any critical information I provide.",
            "While I strive for accuracy, I'm not perfect. Please double-check important details."
        ],
        r".*\bsummarize.*|.*\bsummarization.*": [
            "I can help summarize text or provide concise overviews of content.",
            "I can provide summaries of articles, documents, or other text.",
            "I can create brief summaries to help you understand the main points.",
            "Summarizing content is one of my capabilities."
        ],
        r".*\bsolve.*|.*\bmath.*|.*\bcalculations.*": [
            "I can perform basic math calculations and solve simple problems.",
            "I can help with arithmetic, algebra, and other basic math tasks.",
            "You can ask me to solve math problems or perform calculations.",
            "Math calculations are within my capabilities."
        ],
        r".*\btell me a joke.*|.*\bjoke.*|.*\bfunny.*": [
            "Why don't skeletons fight each other? They don't have the guts!",
            "Sure! Why did the scarecrow win an award? Because he was outstanding in his field!",
            "How about this one: What's orange and sounds like a parrot? A carrot!",
            "Okay! What do you get when you cross a snowman and a vampire? Frostbite!",
            "Here's a classic: Why did the math book look sad? Because it had too many problems!",
            "Sure thing! What do you call a bear with no teeth? A gummy bear!",
            "Of course! Why did the golfer bring two pairs of pants? In case he got a hole in one!",
            "Absolutely! How do you organize a space party? You planet!",
            "Here's one: What's a skeleton's least favorite room in the house? The living room!",
            "Sure! What did one wall say to the other wall? I'll meet you at the corner!",
            "Okay! Why don't scientists trust atoms? Because they make up everything!",
            "How about this one: What's orange and sounds like a parrot? A carrot!",
            "Sure thing! Why did the tomato turn red? Because it saw the salad dressing!",
            "Certainly! What do you call fake spaghetti? An impasta!",
            "Here goes: Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Here's one: How does a penguin build its house? Igloos it together!"]
    }

    for pattern, response_list in responses.items():
        if re.match(pattern, user_input.lower()):
            return random.choice(response_list)

    return "Sorry, I don't understand that."
