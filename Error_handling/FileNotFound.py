
try:
   with open("test1.txt", "r") as f:
    content = f.read()
    print(content)
except FileNotFoundError:
    print("File not found")