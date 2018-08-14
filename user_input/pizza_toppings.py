prompt = "\nPlease enter the topping you want to have on your pizza."
prompt += "\n(Enter 'quit' when finished)"


while(True):
    topping = input(prompt)

    if topping == 'quit':
        break
    else:
        print("I'll add " + topping + " on your pizza.")
