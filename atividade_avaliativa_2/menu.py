from tkinter import *
import subprocess
import os

def abrir_pessoas():
    caminho = os.path.join(os.path.dirname(__file__), "pessoas.py")
    subprocess.run(["python", caminho])

def abrir_veiculos():
    caminho = os.path.join(os.path.dirname(__file__), "veiculos.py")
    subprocess.run(["python", caminho])

def abrir_locais():
    caminho = os.path.join(os.path.dirname(__file__), "locais.py")
    subprocess.run(["python", caminho])

def voltar_login():
    janela.destroy()
    caminho = os.path.join(os.path.dirname(__file__), "login.py")
    subprocess.run(["python", caminho])

janela = Tk()
janela.title("Menu Sistema")
janela.geometry("500x300")

Label(janela, text="MENU PRINCIPAL", font=("Arial", 16, "bold")).pack(pady=20)

frame_botoes = Frame(janela)
frame_botoes.pack(pady=30)

btn1 = Button(frame_botoes, text="Pessoas", command=abrir_pessoas, width=15, height=2)
btn1.grid(row=0, column=0, padx=10, pady=10)

btn2 = Button(frame_botoes, text="Veículos", command=abrir_veiculos, width=15, height=2)
btn2.grid(row=0, column=1, padx=10, pady=10)

btn3 = Button(frame_botoes, text="Locais", command=abrir_locais, width=15, height=2)
btn3.grid(row=1, column=0, padx=10, pady=10)

btn_sair = Button(frame_botoes, text="Sair", command=voltar_login, width=15, height=2)
btn_sair.grid(row=1, column=1, padx=10, pady=10)

janela.mainloop()