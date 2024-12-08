def chatbot():
    print("Hi, I'm a chatbot. Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'exit':
            print("Goodbye!")
            break
        elif 'hello' in user_input:
            print("Chatbot: Hello! How can I assist you?")
        elif 'how are you' in user_input:
            print("Chatbot: I'm doing great, thanks!")
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

chatbot()
