names = ["Jimmy", "Rose", "Max", "Nina", "Phillip"]

for name in names:
    if len(name) != 4:
        continue
    print(f"Hello, {name}")

    if name == "Nina":
        break
print("Done!")

# -----------------------------------------------

count = 5

while count > 0:
    print(count)
    count -= 1

# -----------------------------------------------    

fruits = ["apple", "banana", "orange"]
for list in fruits:
    print(list)    

# -----------------------------------------------

for i in range(2, 11, 2):
    print(i)

# -----------------------------------------------

total = 0

for i in range(1, 101):
    total += i
print(total)    

# -----------------------------------------------

locate = "banana"
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    if fruit == locate:
        print(f"Founded!: {locate}")
        break
else:
    print(f"{locate} not founded")

# -----------------------------------------------

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for number in numbers:
    if number % 2 == 0:
        # Pula os números pares
        continue
    print(f"Número ímpar: {number}")

# -----------------------------------------------

numbers = []

for i in range(1, 5):
    number = float(input(f"Type the {i}° number: "))
    numbers.append(number)

print("Numbers typing: ")
for number in numbers:
    print(number)     