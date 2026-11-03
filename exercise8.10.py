def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(f"Sending message: {current_message}")
        sent_messages.append(current_message)

messages = ["Hai", "How is your day?", "Have a great day!"]
sent_messages = []

send_messages(messages, sent_messages)

print("\nmessages:", messages)
print("sent_messages:", sent_messages)