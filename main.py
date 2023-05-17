from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Create a ChatBot instance
chatbot = ChatBot('MyChatBot')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot on the English corpus
trainer.train('chatterbot.corpus.english')

# Main loop to get user input and generate responses
while True:
    user_input = input("You: ")
    response = chatbot.get_response(user_input)
    print("Bot: ", response)
