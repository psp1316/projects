import random

greetings = ['hello', 'hi', 'hey', 'hola', 'greetings']
questions = ['how are you?', 'how do you do?', 'what is your name?']
responses = ['I am good.', 'I am doing well.', "I'm sorry, but I am a chatbot and don't have a name."]

def chatbot():
    while True:
        user_input = input("You: ")
        if user_input.lower() in greetings:
            print("Chatbot: " + random.choice(greetings))
        elif user_input.lower() in questions:
            print("Chatbot: " + random.choice(responses))
        else:
            print("Chatbot: I'm sorry, I don't understand.")

chatbot()