import os

def deleting_file(file_to_delete):
    if not os.path.exists(file_to_delete):
        print(f"File {file_to_delete} do not exists")
        return
    
    if not os.access(file_to_delete, os.F_OK):
        print(f"File {file_to_delete} do not exists")
        return
    else:
        os.remove(file_to_delete)
        print("File deleted successfuly!")

    
file_to_delete = input("Enter a path: ")
deleting_file(file_to_delete)