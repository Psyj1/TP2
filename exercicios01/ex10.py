#10. Calcular e apresentar o valor do volume de um cilindro, utilizando a formula: VOLUME -> pi * r2 * altura
r = float(input("Ray: "))
h = float(input("Height: "))

pi = 3.14

v = pi * (r ** 2) * h

print(v)