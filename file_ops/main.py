import os

os.makedirs('myfiles', exist_ok=True)
for i in range(5):
    file_name = f'myfiles/{i}.txt'
    with open(file_name, "w") as f:
        f.write(str(i) + "\n")
