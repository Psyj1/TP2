# 3. Leia a tabuada e faça a sequência utilizando while de 1 a 10 mostrando os resultados da tabela
n = int(input("Type an number: "))
i = 1

while i < n:
    eq = n*{i + 1}

    print(f"{n} X {i + 1} = {eq}")