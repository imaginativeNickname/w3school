import math 
import time

def delayed_squareroot(number_input,miliseconds):
    time.sleep(miliseconds/1000)
    return math.sqrt(number_input)

number_input = int(input("Enter a number: "))
miliseconds = int(input("Enter time: "))
number = delayed_squareroot(number_input,miliseconds)

print(f'Square root of {number_input} after {miliseconds} miliseconds is {number}')