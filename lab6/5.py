mylist = list(input("Enter list: ").split())

with open("thisfile.txt","a") as f:
    for i in mylist:
        f.write(i + ' ')

f = open("thisfile.txt")
print(f.read())