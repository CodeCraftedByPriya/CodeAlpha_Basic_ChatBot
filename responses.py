import re
import random


def bot_chats(user_input):
    responses = {
        "hi": [
            "Hello! How can I assist you today?", "Hi there! How can I help you?",
            "Hi! I'm here to help. What do you need assistance with?"
        ],
        "hello": [
            "Hi there! How can I help you?",
            "Hi! I'm here to help. What do you need assistance with?"
        ],
        "hey": [
            "Hey! What can I do for you?",
            "Hi! How can I help you?"
        ],
        "good morning": [
            "Good morning! How may I be of service?", "Hi there! How can I help you?",
            "Hi! I'm here to help. What do you need assistance with?"
        ],
        "good afternoon": [
            "Good afternoon! How can I assist you today?",
            "Good afternoon! What can I do for you?"
        ],
        "good evening": [
            "Good evening! How can I help you?",
            "Good evening! What can I assist you with?"
        ],
        "howdy": [
            "Howdy! What brings you here today?",
            "Howdy! How can I assist you?"
        ],
        "hi there": [
            "Hello! How can I assist you today?",
            "Hi there! How can I help you?"
        ],
        "hey there": [
            "Hi! How can I help you?", "Hi there! How can I help you?",
            "Hi! I'm here to help. What do you need assistance with?"
        ],
        "what's up": [
            "Hey! What can I do for you today?",
            "Hey! How can I assist you?"
        ],
        "hello bot": [
            "Hi! I'm here to help. What do you need assistance with?", "Hi! How can I help you?",
            "Hi there! How can I help you?"
        ],
        "hi assistant": [
            "Hello! How can I assist you today?", "Hi! I'm here to help. What do you need assistance with?",
            "Hi! How can I help you?", "Hi there! How can I help you?"
        ],
        "good day": [
            "Good day! How may I assist you?",
            "Good day! How can I help you?"
        ],
        "hi friend": [
            "Hello! How can I help you today?",
            "Hi there! How can I assist you?"
        ],
        "greetings": [
            "Greetings! What can I do for you?",
            "Greetings! How can I assist you?"
        ],
        "hey bot": [
            "Hey! How can I assist you today?", "Hi! I'm here to help. What do you need assistance with?",
            "Hi! How can I help you?", "Hi there! How can I help you?"
        ],
        "hiya": [
            "Hiya! What brings you here?",
            "Hiya! How can I assist you?"
        ],
        "what is your purpose?": [
            "I'm here to assist you and provide information."
        ],
        "can you explain your functionality?": [
            "My function is to answer questions and provide assistance."
        ],
        "how can you help me?": [
            "I can provide information, answer queries, and offer recommendations."
        ],
        "who are you?": [
            "I'm an AI-powered chatbot designed to assist you."
        ],
        "what services do you offer?": [
            "I provide information, answer questions, and offer assistance."
        ],
        "why should i use your services?": [
            "Our services are designed to provide accurate information and support."
        ],
        "what are your capabilities?": [
            "I can handle various queries and provide relevant information."
        ],
        "how reliable are your responses?": [
            "Responses are based on up-to-date information and algorithms."
        ],
        "tell me about your features.": [
            "My features include providing information and answering questions."
        ],
        "what languages do you understand?": [
            "I understand multiple languages for global accessibility."
        ],
        "how do you handle privacy?": [
            "Privacy is managed according to strict guidelines and protocols."
        ],
        "what is your policy on data security?": [
            "Data security is a top priority, ensuring protection and confidentiality."
        ],
        "what kind of information can you provide?": [
            "I provide information on various topics and queries."
        ],
        "how do you ensure accuracy?": [
            "Accuracy is ensured through verified sources and algorithms."
        ],
        "can you assist with technical issues?": [
            "I can offer guidance on technical issues and troubleshooting."
        ],
        "tell me a joke": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "can you tell me a joke?": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "give me a joke": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "i want to hear a joke": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "share a joke": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "make me laugh": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "joke please": [
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
            "Here's one: How does a penguin build its house? Igloos it together!"
        ],
        "can you entertain me with a joke?": [
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
