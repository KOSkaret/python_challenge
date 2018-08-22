print('Enter q at any time to quit.')

while True:

    try:
        x = input("Write in a first number: ")
        if x == 'q':
            break
        x = int(x)
        y = input("Write a second number: ")
        if y == 'q':
            break
        y = int(y)
        z = x + y

    except ValueError:
        print("This is not a number!")

    except TypeError:
        print("This is not a number!")
    else:
        print("The result of adding " + str(x) + " and " + str(y) + " is " + str(z) + '\n')