#3. Leia 6 nomes de Capitais do Brasil e guarde numa matriz [2,3] e mostre todas as capitais
l = int(input("Type the quantity of lines: "))
c = int(input("Type the quantity of collums: "))

m = []
for i in range(l):
    li = []
    m.append(li)
    for j in range(c):
        number = float(input(f"Type an capital: "))
        li.append(number)

for line in m:
    print(' '.join(map(str, line)))