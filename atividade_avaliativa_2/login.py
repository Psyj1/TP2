from tkinter import *
from tkinter import messagebox
import subprocess
import os

tela = Tk()
tela.title("Login")
tela.geometry("400x200")
tela.resizable(False, False)

def sair():
    if messagebox.askyesno("Sair", "Deseja sair?"):
        tela.destroy()

def entrar():
    usuario = txt_user.get()
    senha = txt_senha.get()
    
    if usuario == "admin" and senha == "123":
        tela.destroy()
        caminho = os.path.join(os.path.dirname(__file__), "menu.py")
        subprocess.run(["python", caminho])
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos!")


lar_tela = tela.winfo_screenwidth()
alt_tela = tela.winfo_screenheight()
x = (lar_tela - 400) // 2
y = (alt_tela - 200) // 2
tela.geometry(f"400x200+{x}+{y}")

Label(tela, text="Usuário:").place(x=50, y=40)
Label(tela, text="Senha:").place(x=50, y=80)

txt_user = Entry(tela, width=25)
txt_user.place(x=120, y=40)

txt_senha = Entry(tela, width=25, show="*")
txt_senha.place(x=120, y=80)

btn_entrar = Button(tela, text="Entrar", command=entrar, width=10)
btn_entrar.place(x=150, y=120)

btn_sair = Button(tela, text="Sair", command=sair, width=10)
btn_sair.place(x=250, y=120)

tela.mainloop()