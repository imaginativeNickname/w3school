import re

string = input("Enter a string: ")

def finding(string):
    pattern = '^a.*b$'
    if re.match(pattern, string):
        print("Match found")
    else:
        print("Match not found")

finding(string)