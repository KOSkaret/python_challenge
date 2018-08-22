filename = 'learning_python.txt'

replace = 'Python'
replace_with = 'C'

with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.replace(replace,replace_with).rstrip())