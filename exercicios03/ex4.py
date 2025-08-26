# 4. Construa um programa que solicite ao operador do caixa o preço total da compra, bem como a forma de pagamento. Ao fim, o programa deve informar o valor de compra e valor final a ser pago com desconto
c = int(input("Type the format of payment \n 1- Vista \n 2- Debit Card \n 3- Credit card:"))

match c:
    case 1:
        p = float(input("Type value of the product: "))
        r = p + (p*0.15)

        print(f"Final value {r}")
    case 2:
        p = float(input("Type value of the product: "))
        r = p + (p*0.10)

        print(f"Final value {r}")
    case 3:
        p = float(input("Type value of the product: "))
        r = p + (p*0.05)

        print(f"Final value {r}")
    case _:
        print("Invalid option")        