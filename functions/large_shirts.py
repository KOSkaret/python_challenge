def make_shirts(size='L', message='I love python'):
    # Make a function, default values are 'L' and 'I love python'
    """ Make shirts off the size or message that the user wants. """
    # The code surrounded with """ """ is the docstring
    print("Hello! the shirt you have ordered is of size " + size + ".")
    print("The messsage on the shirt are " + message + ".\n")

# Regular function call.
make_shirts('XL', 'Supreme')
# Function call with keyword arguments
make_shirts(message='Pretentious', size= 'M')
# Function call with one word and rest default.
make_shirts('M')
make_shirts()
# Function call with one keyword argument and default t-shirt size.
make_shirts(message='IT-monkey')
