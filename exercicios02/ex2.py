# 2. Construa um programa que receba um número inteiro positivo informado pelo usuário. Caso ele seja par, o programa deve calcular seu quadrado. Mas, se ele for ímpar, deve ser calculado o seu cubo. Ao fim, o programa deve mostrar o valor caclulado e dizer se o número é impar ou par

n = int(input("Digite um número:"))

if n % 2 == 0:
    print(f'O valor é par, e o valor é {n**2}')
else:
    print(f"O valor é ímpar, e o valor é {n**3}")    