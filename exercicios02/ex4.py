n1 = int(input("Digite numero 1:"))
n2 = int(input("Digite numero 2:"))

if n1 < 0 or n2 < 0:
    print("Um dos números são negativos, tente outros valores!")
else:
    print('Escolha uma das três opções \n 1. Média Ponderada(peso 2 e 3) \n 2. Quadrado da soma dos 2 números \n 3. Cubo do menor múmero')
    o = int(input('Escolha uma opção: '))

    if o == 1:
        mp = (n1 * 2 + n2 * 3)/5
        print(f'{mp}')
    elif o == 2:
        q = (n1+n2)**2
        print(f'{q}')
    elif o == 3:
        if n1 < n2:
            c = n1 ** 3
            print(f'{c}')
        else:
            c = n2 ** 3
            print(f'{c}')
    else:
        print("Opção inválida")