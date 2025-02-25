import re

string = input("Enter a string: ")

def split_to_uppercase(string):
    pattern = '(?=[A-Z])'
    result = re.split(pattern,string)
    print(result)

split_to_uppercase(string)