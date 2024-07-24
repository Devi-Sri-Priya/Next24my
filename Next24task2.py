import nltk
from nltk.chat.util import Chat, reflections

# Define pairs of patterns and responses
pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how are you today?",]
    ],
    [
        r"what is your name?",
        ["My name is ChatBot and I'm here to help you.",]
    ],
    [
        r"how are you?",
        ["I'm doing good. How about you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright", "No problem at all",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Nice to hear that!", "Alright, great!",]
    ],
    [
        r"quit",
        ["Bye, take care.", "Goodbye!"]
    ],
]

# Create a chatbot using the defined pairs and reflections
chatbot = Chat(pairs, reflections)

# Main function to interact with the chatbot
if __name__ == "__main__":
    print("Hello! I am a chatbot. Type 'quit' to end the conversation.")
    chatbot.converse()
