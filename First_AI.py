from flask import Flask, jsonify, request
import random
import json
import nltk
from nltk.tokenize import word_tokenize
from flask_cors import CORS
from datetime import datetime

nltk.download('punkt')

app = Flask(__name__)
CORS(app)

file_path = "contents.json"

def parse_json_file(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        print(f"Error: File not found at {file_path}. Make sure the path and file are correct.")
        exit()
    except json.JSONDecodeError:
        print(f"Error: Invalid JSON format in the file {file_path}.")
        exit()
    except Exception as e:
        print(f"Error while reading the file: {e}")
        exit()

contents = parse_json_file(file_path)

jokes = [
    "Why don't skeletons fight each other? They don't have the guts!",
    "I told my computer I needed a break, and it froze!",
    "Why did the scarecrow win an award? Because he was outstanding in his field!"
]

def tell_joke():
    return random.choice(jokes)

def chatbot_response(user_input):
    user_input_lower = user_input.lower().strip()

    for section, items in contents.items():
        for key, description in items.items():
            if key in user_input_lower:
                return description

    tokens = word_tokenize(user_input_lower)
    greetings = ["hello", "hi"]
    farewells = ["bye", "goodbye", "see you"]
    help_phrase = ["can you help me", "i need help", "help me", "help"]
    saltation = ["how are you", "how are u", "how do you do"]
    asking = ["what are you doing", "what are you up to"]
    greet_back = ["i am good", "fine", "good", "i am good","i am fine"]
    thanking = ["thank you", "tq", "thank u"]
    sad_words = ["sad", "unhappy", "down", "depressed", "blue", "sorrow", "bored"]
    happy_words = ["happy", "excited", "joyful", "elated", "ecstatic", "content", "cheerful"]
    
    if "play" in user_input_lower or "game" in user_input_lower:
        return "You can play 'Guess the Number' game here!"
    
    if any(word in tokens for word in sad_words):
        return "I'm sorry you're feeling down. Here’s a joke to cheer you up: " + tell_joke()
    
    if any(word in tokens for word in happy_words):
        return "I’m glad you're feeling good! Keep the positivity flowing!"
            
    if any(word in tokens for word in greetings):
        return random.choice([
            "Hi there! How are you?",
            "Hi! How's your day?",
            "Hey! What's up with you?",
        ])
        
    if any(phrase in user_input_lower for phrase in thanking):
        return random.choice([
            "You're welcome!",
            "No problem at all!",
            "Happy to assist!",
            "Glad I could help!"
        ])
        
    if "how many states are in india" in user_input_lower or "total number of states in india" in user_input_lower or "states in india" in user_input_lower:
        return "There are 28 states and 8 union territories in India."
    
    if "name them" in user_input_lower:
        states = [
            "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa",
            "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala",
            "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland",
            "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura",
            "Uttar Pradesh", "Uttarakhand", "West Bengal"
        ]
        return f"The 28 states of India are: {', '.join(states)}."
    
    elif any(phrase in user_input_lower for phrase in greet_back):
        return random.choice([
            "Great!!",
            "Glad to hear that!",
            "Wonderful",
        ])

    elif any(word in tokens for word in farewells):
        return random.choice([
            "I look forward to our next meeting.",
            "Looking forward to our future discussions.",
            "It was a pleasure connecting with you."
        ])
    elif any(phrase in user_input_lower for phrase in help_phrase):
        return random.choice([
            "Of course! What do you need assistance with?",
            "Absolutely! How may I assist you today?",
            "Definitely! How can I be of service?"
        ])
    elif any(phrase in user_input_lower for phrase in saltation):
        return random.choice([
            "I’m doing well, thank you for asking. How about you?",
            "Thank you for asking! I’m well, and I hope you are too.",
            "I’m good, thank you. How can I assist you today?"
        ])
    elif any(phrase in user_input_lower for phrase in asking):
        return random.choice([
            "I'm currently waiting for your question.",
            "I'm ready to assist you with any inquiries you might have.",
            "Just processing information and ready to help!"
        ])
    else:
        return f"Hello! I couldn't understand that. You can ask me about Indian capitals, cricketers, or famous places."

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    if user_input:
        response = chatbot_response(user_input)
        return jsonify({"response": response})
    return jsonify({"error": "Invalid input"}), 400


if __name__ == '__main__':
    app.run(debug=True)