import re

string = input("Enter a string: ")

def finding_uppercase(string):
    pattern = '[A-Z][a-z]+'
    if re.findall(pattern,string):
        print("Match found")
    else:
        print("Match not found")

finding_uppercase(string)