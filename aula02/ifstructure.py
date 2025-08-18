#Estrutura condicional if, é uma estrutura de comparação para verificar determinadas condições
entrada = input("Você quer entrar ou sair?")

if entrada == 'entrar':
    print("Você entrou no sistema!")
elif entrada == 'sair':
    print('Você saiu do sistema')
else:
    print('Você não digitou um valor inválido')