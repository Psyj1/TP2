#5. Crie um vetor para digitar nomes de times de futebol, sem especificar o tamanho do vetor e mostrar os nomes dos times no final
type = input("Type the teams, separated for space")

teams = [str(x) for x in type.slipt()]

print(teams)