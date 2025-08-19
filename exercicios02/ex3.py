# 3. Escreva um programa que solicite ao usuário a estatura de 3 pessoas. Ao fim, o programa deve mostrar as estaturas em ordem decrescente

e1 = float(input("Estatura 1: "))
e2 = float(input("Estatura 2: "))
e3 = float(input("Estatura 3: "))

if e1 > e2 and e1 > e3:
    if e2 > e3:
        print("1. Estatura 1 \n 2. Estatura 2 \n 3. Estatura 3")
    else: 
        print("1. Estatura 1 \n 2. Estatura 3 \n 3. Estatura 2")
if e2 > e1 and e2 > e3:
    if e1 > e3:
        print("1. Estatura 2 \n 2. Estatura 1 \n 3. Estatura 3")
    else: 
        print("1. Estatura 2 \n 2. Estatura 3 \n 3. Estatura 1")
else:
    if e1 > e2:
        print("1. Estatura 3 \n 2. Estatura 1 \n 3. Estatura 2")
    else: 
        print("1. Estatura 3 \n 2. Estatura 2 \n 3. Estatura 1")