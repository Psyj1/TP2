lines = int(input("Type the quantity of lines: "))
collums = int(input("Type the quantity of collums: "))

mat = []
for i in range(lines):
    line = []
    mat.append(line)
    for j in range(collums):
        number = float(input(f"Type the number of position ({i}, {j})"))
        line.append(number)

for line in mat:
    print(' '.join(map(str, line)))
