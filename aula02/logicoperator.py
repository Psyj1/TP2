n1 = int(input("Digite o primeiro número:"))
n2 = int(input("Digite o segundo número:"))
n3 = int(input("Digite o terceiro número:"))

if n1 == n2 or n2 == n3 or n1 == n3:
    exit() #encerra o programa
if n1 > n2 and n1 > n3:
    print("O primeiro número é maior")
if n2 > n1 and n2 > n3:
    print("O segundo número é maior") 
if n3 > n1 and n3 > n2:
    print("O terceiro número é maior")