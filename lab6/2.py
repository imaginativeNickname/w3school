import os

if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    with open("myfile.txt","x") as f:
        with open("myfile.txt","w") as f:
            f.write(input())
            f.close()
        with open("myfile.txt","r") as f:
            print(f.read())
