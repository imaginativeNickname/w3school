import re

string = input("Enter a string: ")

def replace(string):
    pattern = '_[A-Za-z]'
    string = re.sub(pattern, lambda x: x.group(0)[1].upper(),string)
    print(string)

replace(string)