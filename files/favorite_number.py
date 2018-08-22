import json

def get_favorite_number(filename):
    """Get stored number if available."""
    try:
        with open(filename) as f_obj:
            number = json.load(f_obj)
    except FileNotFoundError:
        return None
    else:
        return number

def get_new_number(filename):
    """Prompts for a new favorite number."""
    number = input("What is your favorite number? ")

    with open(filename, 'w') as f_obj:
        json.dump(number, f_obj)
    
    return number

def tell_fav_number():
    """Share the user darkest secrets, their favorite number"""
    filename = 'number.json'
    number = get_favorite_number(filename)

    if number:
        print("I know your favorite number! It's " + str(number))
    else:
        number = get_new_number(filename)
        print("I'll remember you darkest secret, the number " + number +
        "! Ha!")

tell_fav_number()