import re

string = input("Enter a string: ")
def replacer(string):
    pattern = '[ .,]'
    string = re.sub(pattern,'|',string)
    print(string)

replacer(string)