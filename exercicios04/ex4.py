#4. Crie um vetor para ler 5 cores mostre as cores armazenadas no vetor
s = int(input("Type an size of vector: "))

vector = []

for i in range(s):
    element = int(input(f"Type an color: "))
    vector.append(element)

print("Colors:", vector) 