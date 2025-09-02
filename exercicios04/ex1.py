#1. Crie um vetor, leia 10 posições de números inteiros, armazene os valores e mostre

size = int(input("Type an size of vector: "))

vector = []

for i in range(size):
    element = int(input(f"Type an element for {i + 1}° position: "))
    vector.append(element)

print("Vector:", vector) 