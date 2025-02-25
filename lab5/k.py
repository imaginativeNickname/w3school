import re

string = input("Enter a string: ")

def camel_to_snake(string):
    pattern = r'([a-z])([A-Z])'
    result = re.sub(pattern, r'\1_\2', string).lower()
    print(result)

camel_to_snake(string)