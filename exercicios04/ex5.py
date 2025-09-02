#5. Crie um vetor para digitar nomes de times de futebol, sem especificar o tamanho do vetor e mostrar os nomes dos times no final
s = int(input("Type an size of vector: "))

teams = []

for i in range(s):
    element = int(input(f"Type an Football team: "))
    teams.append(element)

print("Football teams:", teams) 