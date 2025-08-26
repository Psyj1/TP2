#1. Faça um programa que verifique se uma letra digitada é consoante ou vogal
l = input("Type an letter: ")

match l.lower():
    case "a" | "e" | "i" | "o" | "u":
        print("It's a vogal!")                           
    case _:
        print("It's a consoant!")