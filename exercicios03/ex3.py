# 3. Construir um programa que apresente o menu com os cálculos de tensão, resistência e corrente
c = int(input("Choose an option to make a equation: \n 1- Tension(in volts) \n 2- Resist(in Ohm) \n 3- Corrent(in Amper): "))

match c:
    case 1:
        r = float(input("Type the value to resistance: "))
        i = float(input("Type the value to corrent: "))

        U = r * i

        print(f"The value of tension in Amper is {U}")
    case 2:
        u = float(input("Type the value to tension: "))
        i = float(input("Type the value to corrent: "))

        R = u / i

        print(f"The value of tension in Amper is {R}")
    case 3:
        u = float(input("Type the value to tension: "))
        r = float(input("Type the value to resistance: "))

        I = u / r

        print(f"The value of tension in Amper is {I}")
    case _:
        print("Invalid option!")    