choices = int(input("Enter number of choices:"))
data = []
for i in range(choices):
    data_input = str(input(f'Enter the name {i+1}:'))
    data.append(data_input)

print("The names you entered are:", data)