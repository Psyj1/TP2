from tkinter import *

tela = Tk()

# Título na barra de tarefas
tela.title("Fatec Registro")

# Configuração da cor da tela (opcional)
tela.configure(background= '#1e3743')
# Configuração do tamanho da tela
tela.geometry("700x600")

tela.resizable(True, True)
# Tamanho maximo que a tela pode chegar
tela.maxsize(width=800, height=700)
# Tamanho mínimo que a tela pode chegar
tela.minsize(width= 500, height=300)

lbl_teste = Label (tela, text="TESTE").place (x=10, y=10)
# lbl_teste e o nome da identificaçãi interna da label
# Label e o tipo de componente
# tela a variavel que a label está ligado
# text="" e o texto a ser exibido na tela
# place o posicionamento da tela

lbl_nome = Label(tela, text="Nome").place (x=10, y=10)
lbl_cpf = Label(tela, text="CPF").place (x=10, y=50)

tela.mainloop()