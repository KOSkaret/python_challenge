file_name = 'guest_book.txt'

def greeter():
    print('Welcome to our hotel!')
    print('Please write your name in the guest book')
    print('If done, please exit by writing q in the prompt')

with open(file_name,'a') as file_object:
    greeter()
    while True:
         text_input = input("Your name: ")
         if text_input == 'q':
            break
         print('Welcome to our hotel dear ' + text_input)
         file_object.write(text_input + '\n')