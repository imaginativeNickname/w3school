import os

path = input("Enter path: ")

if os.path.exists(path):
    filename = os.path.basename(path)
    directory = os.path.dirname(path)

    print(f'filename = {filename}')
    print(f"direcory = {directory}")
else:
    print("Path does not exist")