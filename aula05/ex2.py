from tkinter import *

tela = Tk()

tela.title("Fatec Registro")

# dimensoes da janela
largura = 800
altura = 300

# resolucao do sistema(tela)
largura_screen = tela.winfo_screenwidth()
altura_screen = tela.winfo_screenwidth()

posx = largura_screen/2 - largura/2
posy = altura_screen/2 - altura/2

# vizualizacao do tamanho da tela do terminal
print(largura_screen, altura_screen)

# definicao do geometry
tela.geometry("%dx%d+%d+%d" % (largura, altura, posx, posy))
tela.mainloop()