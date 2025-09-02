#6. Crie um vetor que leia valores inteiros, e mostre os valores armazenados, e mostre quais são pares
s = int(input("Type an size of vector: "))

teams = []

for i in range(s):
    element = int(input(f"Type an Football team: "))
    teams.append(element)

print("Football teams:", teams) 