filename = 'learning_python.txt'

def print_object():
    with open(filename) as file_object:
        for line in file_object:
            print(line.rstrip())

# print_object()
# print_object()
# print_object()


with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())