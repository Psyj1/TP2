#11. Leia a descrição do produto (nome), a quantidade comprada e o preço unitário. Calcular e escrever o total e a descrição do produto

n = input("Name: ")
q = float(input("Quantity: "))
p = float(input("Price: "))

t = q * p

print(f"The name of the product is {n}, and the total price is {t}")