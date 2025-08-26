# 2. A Secretária de Meio Ambiente, que controla o índice de poluição, mantém três grupos de indústrias que são altamente poluentes do meio ambiente. A tabela a seguir indica a ação a ser tomada pela Secretaria de  acordo com o pindice de poluição, leia o índice de poluição
i = int(input("Type the indice? of polution: "))

match i:
    case 0 | 1 | 2:
        print("Considering acceptable")
    case 3 | 4 | 5:
        print("Suspend activitty group 1")
    case 6 | 7:
        print("Suspend activitty group 1 AND 2")
    case _:
        print("Suspend activitty of ALL groups!")        