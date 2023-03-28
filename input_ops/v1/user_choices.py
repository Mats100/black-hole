data = []
choices = int(input("Enter number of choices:"))
for i in range(choices):
    name_input = str(input(f'Enter the name {i + 1}:'))
    data.append(name_input)
print("The names you entered are:", data)

scores = {}
for i, name in enumerate(data):
    print(f"\n{name}, Enter scores for each user (including yourself):")
    for j, other_user in enumerate(data):
        while True:
            score = input(f"Score for {other_user}: ")
            if score.isdigit() and 0 <= int(score) <= 10:
                break
            else:
                print("Invalid score, Please enter a number between 0 and 10.")
        scores[(i, j)] = int(score)

print("\nTotal Scores:")
for i, name in enumerate(data):
    user_score = sum([scores[(j, i)] for j in range(choices) if j != i])
    user_score += scores[(i, i)]
    print(f"{name} got a total score : {user_score}")