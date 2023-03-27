data = []
choices = int(input("Enter number of choices:"))
for i in range(choices):
    name_input = str(input(f'Enter the name {i + 1}:'))
    data.append(name_input)
print("The names you entered are:", data)

scores = {}
for i, name in enumerate(data):
    print(f"\n{name}, enter scores for each user (including yourself):")
    total_score = 0
    for j, other_user in enumerate(data):
        while True:
            score = input(f"Score for {other_user}: ")
            if score.isdigit() and 0 <= int(score) <= 10:
                break
            else:
                print("Invalid score, please enter a number between 0 and 10.")
