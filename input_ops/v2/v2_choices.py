scores = {}
while True:
    choices = int(input("Enter number of choices:"))
    if choices == 1:
        print("Choices must be greater than 1")
        break
    for i in range(choices):
        name_input = str(input(f'Enter the name {i + 1}:'))
        scores.update({name_input: 0})

    for i, name in scores.items():
        print(f"\n{i}, Enter scores for each user (including yourself):")
        for j, other_user in scores.items():
            if i == j:
                continue
            while True:
                score = input(f"Score for {j}: ")
                if score.isdigit() and 0 <= int(score) <= 10:
                    scores[j] = scores[j] + int(score)
                    break
                else:
                    print("Invalid score, Please enter a number between 0 and 10.")
    print(scores)
    break
