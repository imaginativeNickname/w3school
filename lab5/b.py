import re

string2 = input("Enter a string: ")

def finite_matches(string2):
    smash = 'ab{2,3}'
    if re.match(smash,string2):
        print("Match found")
    else:
        print("Match not found")

finite_matches(string2)