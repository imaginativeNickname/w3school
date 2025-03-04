def counting_lines(filename):
    with open(filename,"r") as f:
        lines = f.readlines()
        return len(lines)
    
filename = input()
print(f"Number of lines = {counting_lines(filename)}")