#12. Calcule quantos azulejos são necessários para azulejar uma parede. É necessário conhecer a altura da parede, a sua largura, e a altura do azulejo e a sua largura. Leia os dados em seguida e calcule a área da parede, e do azulejo, e em seguida calcule a quantidade de azulejos necessários.
hw = float(input("Height wall: "))
lw = float(input("Large wall: "))

ha = float(input("Height azulejo??: "))
la = float(input("Large azulejo??: "))

aw = (hw*lw)/2
aa = (ha*la)/2

at = aw/aa

print(aw)
print(aa)
print(at)