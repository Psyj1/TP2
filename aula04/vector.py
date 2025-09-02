vector = [10, 20, 30, 40]
print(vector)

# -----------------------------------------------

tam = int(input("Type an size of vector: "))

vector1 = []

for i in range(tam):
    element = int(input(f"Type an element for {i + 1}° position: "))
    vector1.append(element)

print("Vector:", vector1)    

# -----------------------------------------------

phrase = "This is a example phrase"

letters = phrase.split()
print(letters)

# -----------------------------------------------

address = "Av. Clara Gianotti de Souza, 250, Centro, Registro, SP"
letters1 = address.split(", ")

print(letters1)

print(f"The name of the avenue is: {letters1[0]}")
print(f"The number of the address is: {letters1[1]}")

# -----------------------------------------------

entrance = input("Type the elements of vector separated per space: ")

vector2 = [int(x) for x in entrance.split()]

print(vector2)

# -----------------------------------------------

mat = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Element of the first line and second collum:", mat[0][0])
print("Element of the second line and third collum:", mat[1][2])
print("Element of the third line and second collum:", mat[2][1])

print("Matriz:")
for line in mat:
    print(line)

# -----------------------------------------------

    