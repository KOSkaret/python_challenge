# importing the json library.
import json

# make a filepath with the json file extension.
filename = 'numbers.json'

with open(filename) as f_obj:
    numbers = json.load(f_obj)

print(numbers)