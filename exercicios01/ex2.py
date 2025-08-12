#2 Construa um programa que receba do usário a variação do deslocamento de um objeto (em metros) e a variação do tempo percorrido (em segundo). Ao fim, o programa deve calcular a velocidade média, em m/s, do objeto(vm = d/t)
d = float(input("Type the distance of the object: "))
t = float(input("Type the time wasted of object: "))

vm = d/t
print (f"Media Velocity: {vm}")