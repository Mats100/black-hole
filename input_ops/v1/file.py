name = input("Enter the name you want to search for: ")
with open("output.txt", "r") as f:
    lines = f.readlines()

found = False
for line in lines:
    if name in line:
        print(line.strip())
        found = True
        break
if not found:
    print(f"No record found for {name}")
