lower = 0
upper = 0
str = input("Enter a string: ")

for x in str:
    if(x.islower()):
        lower+=1
    else:
        upper+=1
    
print(f'lower cases = {lower}')
print(f'upper cases = {upper}')