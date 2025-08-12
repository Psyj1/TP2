#9. Leia o número de votos brancos, nulos e válidos. Faça a soma do número total de eleitores. Calcular e escrever o percentual que cada um representa, em relação ao total de eleitores
b = int(input("White votes: "))
n = int(input("Null votes: "))
v = int(input("Valid votes: "))

t = b + n + v

pb = (b*100)/t
pn = (n*100)/t
pv = (v*100)/t

print(pb)
print(pn)
print(pv)