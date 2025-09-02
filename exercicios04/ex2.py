#2. Crie uma matriz [4,4] de insetos que leia 16 valores, conte e escreva quantos valores maiores que 10 a matriz possui
l = int(input("Type the quantity of lines: "))
c = int(input("Type the quantity of collums: "))

m = []
for i in range(l):
    li = []
    m.append(li)
    for j in range(c):
        number = float(input(f"Type the number of position ({i}, {j})"))
        li.append(number)

for line in m:
    print(' '.join(map(str, line)))