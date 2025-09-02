import numpy as np

size = int(input("Type a size of vector: "))

vector = np.empty(size, dtype=int)

for i in range(size):
    element = int(input(f"Type an element {i + 1}° in vector: "))
    vector[i] = element

print("Vector:", vector)    