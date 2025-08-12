#Todos os meus códigos estarão em inglês, a fim de utilizar de boas práticas/tecnicas de programação
#Examplo 1

name = "Maylon"
age = 15

#print(name)

#Examplo 2

first_value = input("Type the first value: ")
second_value = input ("Type the second value: ")
print(first_value + "\n" + second_value)

#Exemplo 2 correto

first_value = int(input("Type the first value: "))
second_value = int(input ("Type the second value: "))
sum = first_value + second_value
print(f"The value of the sum is {sum}")

#Desafio: programa para calcular a área de um triangulo

b = float(input("Type the value of the base of the triangle: "))
h = float(input("Type the value of the height of the triangle: "))
a = (b*h)/2
print(f"Result: {a:.2f}")