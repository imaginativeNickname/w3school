import re

string3 = input("Enter a string: ")

def fining_lowercase(string3):
    I_found_it = '[a-z_]*'
    if re.match(I_found_it,string3):
        print("Match found")
    else:
        print("Match not found")

fining_lowercase(string3)