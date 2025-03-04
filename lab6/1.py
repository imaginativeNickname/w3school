import os

f = open("demofile.txt","w")
f.write("Woops! I have deleted the content!")
f.close()

f = open("myfile.txt","x")

