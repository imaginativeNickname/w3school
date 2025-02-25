import re

string = input("Enter a string: ")
def insert_spaces(string):
    pattern = '([a-z])([A-Z])'
    result = re.sub(pattern, r'\1 \2', string)
    print(result)

insert_spaces(string)