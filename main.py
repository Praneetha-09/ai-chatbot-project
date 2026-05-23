import datetime

print("AI Chatbot Started...")
print("Type 'bye' to stop the chatbot.")

while True:

    user = input("\nYou: ").lower()

    if user == "hi":
        print("Bot: Hello!")

    elif user == "hello":
        print("Bot: Hi there!")

    elif user == "good morning":
        print("Bot: Good morning!")

    elif user == "good evening":
        print("Bot: Good evening!")

    elif user == "how are you":
        print("Bot: I am fine. How are you?")

    elif user == "i am fine":
        print("Bot: Nice to hear that!")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who created you":
        print("Bot: I was created using Python.")

    elif user == "what can you do":
        print("Bot: I can answer simple questions and chat with you.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is machine learning":
        print("Bot: Machine Learning helps computers learn from data.")

    elif user == "what is python":
        print("Bot: Python is a programming language used in AI.")

    elif user == "what is chatbot":
        print("Bot: A chatbot is a program that talks with users.")

    elif user == "tell me a joke":
        print("Bot: Why did the computer get cold? Because it left its Windows open!")

    elif user == "do you like music":
        print("Bot: Yes, music is amazing!")

    elif user == "which is your favorite color":
        print("Bot: My favorite color is blue.")

    elif user == "who is your favorite hero":
        print("Bot: I like Iron Man.")

    elif user == "time":
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    elif user == "date":
        today = datetime.date.today()
        print("Bot: Today's date is", today)

    elif user == "motivate me":
        print("Bot: Believe in yourself. You can achieve great things!")

    elif user == "i am tired":
        print("Bot: Take some rest and come back stronger!")

    elif user == "i love coding":
        print("Bot: That's great! Coding is fun and powerful.")

    elif user == "exam stress":
        print("Bot: Stay calm, prepare well, and do your best.")

    elif user == "which is best programming language":
        print("Bot: Python is one of the best languages for beginners.")

    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break

    else:
        print("Bot: Sorry, I don't understand that.")