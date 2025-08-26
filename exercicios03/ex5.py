# 5. Faça um algoritimo que leia a categoria e salário de um empregado.
c = int(input("Choose your category? \n 1- A \n 2- B \n 3-C: "))

match c:
    case 1:
        s = float(input("How much do you earn per month?"))

        r = s + (s*0.10)

        print(f"The new salary is {r}")
    case 2:
        s = float(input("How much do you earn per month?"))

        r = s + (s*0.15)

        print(f"The new salary is {r}")
    case 3:
        s = float(input("How much do you earn per month?"))

        r = s + (s*0.25)

        print(f"The new salary is {r}")        
    case _:
        print("Invalid option")