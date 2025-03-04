import shutil

shutil.copy('demofile.txt','myfile.txt')

with open("demofile.txt") as first, open("myfile.txt","w") as second:
    for i in first:
        second.write(i)