#6. Escreva um algoritimo para ler o salário mensal atual de um funcionário e o percentual de reajuste. Calcular e escrever o valor do novo salário
s = float(input("How much do you receive?"))
p = float(input("What is the percentual of the lost?"))

r = s-(s*p)

print(f"{r}")