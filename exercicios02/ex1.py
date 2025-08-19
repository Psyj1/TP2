#1. Construa um programa que receba o peso de duas pessoas e diga qual a pessoa mais pesada e verifica se as pessoas tem o mesmo peso.

p1 = float(input("Peso pessoa 1: "))
p2 = float(input("Peso pessoa 2: "))

if p1 == p2:
    print("Mesmo peso")
elif p1 > p2:
    print("Pessoa 1 é mais pesada")
else: 
    print("Pessoa 2 é mais pesada")        
