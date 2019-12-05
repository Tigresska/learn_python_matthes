promt = """
What pizza ingredient do you want to add?
Enter 'quit' to end the program. """
active = True
toppings = []
while active:
    message = input(promt)

    if message.lower() == 'quit':
        active = False
    else:
        #print(message)
        toppings.append(message)
        print(f"The ingredients of your pizza: {toppings}")
