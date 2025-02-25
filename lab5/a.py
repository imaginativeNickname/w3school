import re

string = input("Enter a string: ")

def infinite_matches(string):
    pattenr = 'ab*'
    if re.match(pattenr,string):
        print("Match found")
    else:
        print("Match not found")

infinite_matches(string)

