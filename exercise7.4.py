prompt = "What topping would you like on your pizza:"
prompt += " (Enter 'quit' when you are finished) "

while True:
    topping = input(prompt)
    
    if topping.lower() == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza!")