# 6- Escreva um programa que leia um peso de uma pessoa na Terra e o número de um planeta e mostre o valor do seu peso neste planeta é dada a seguir juntamente com o valor das gravidades relativas á Terra
p = int(input("Choose an option: \n 1-Mercury \n 2-Vênus \n 3-Mart \n 4-Jupiter \n 5- Saturn: "))

match p:
    case 1:
        w = float(input("What is your weight?"))

        fw = w * 0.37

        print(f"Your weight is {fw}")
    case 2:
        w = float(input("What is your weight?"))

        fw = w * 0.88

        print(f"Your weight is {fw}")
    case 3:
        w = float(input("What is your weight?"))

        fw = w * 0.38

        print(f"Your weight is {fw}")
    case 4:
        w = float(input("What is your weight?"))

        fw = w * 2.64

        print(f"Your weight is {fw}")
    case 5:
        w = float(input("What is your weight?"))

        fw = w * 1.15

        print(f"Your weight is {fw}")                
    case _:
        print("Invalid option")