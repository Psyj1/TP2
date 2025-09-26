# Crie uma interface gráfica em Python utilizando Tkinter para simular um cadastro de familiares.
#   Requisitos da aplicação:
#       1. Campos de entrada de texto:
#           ○ Nome
#           ○ Idade
#           ○ Telefone
#           ○ Grau de parentesco
#           ○ Mais algum campo (opcional)
#       2. Botão "Cadastrar":
#           ○ Ao clicar, os dados informados pelo usuário devem ser adicionados
#              imediatamente abaixo em uma label ou área de exibição, mostrando todos os familiares cadastrados.
#              Também deverá mostrar se a pessoa é maior ou não, de idade.
#       3. Dados iniciais:
#           ○ A aplicação deve iniciar já com pelo menos 4 familiares cadastrados (exemplo: pai, mãe, irmão, avô).
#       4. Critérios de avaliação:
#           ○ Funcionalidade
#           ○ Legibilidade do código
#           ○ Comentários explicativos
#           ○ Interface visual
#           ○ Dados iniciais corretos
#           ○ Criatividade e melhorias extras (cálculo de idade, pessoa maior ou não de idade, pode ou não votar)


import tkinter as tk
from tkinter.ttk import Combobox
from tkinter import filedialog
from PIL import Image, ImageTk
from tkinter import Button

pasta_inicial = ""

familiares = [
    {"nome": "André", "idade": "50", "telefone": "1111-1111", "grau": "Pai", "cidade": "Iguape"},
    {"nome": "Nicolle", "idade": "47", "telefone": "2222-2222", "grau": "Mãe", "cidade": "Iguape"},
    {"nome": "Lucas", "idade": "22", "telefone": "3333-3333", "grau": "Primo", "cidade": "Registro"},
    {"nome": "João", "idade": "75", "telefone": "4444-4444", "grau": "Tio", "cidade": "Cajati"},
]


tela = tk.Tk()
tela.title("open file")
tela.geometry("700x700")

combo = Combobox(tela)
combo['values'] = ("Iguape", "Ilha Comprida", "Registro", "Juquiá", "Miracatu", "Cajati")
combo.current(1)
combo.pack()

def show():
    tk.Label(tela, text=var.get()).pack()    

var = tk.StringVar()

chk_button = tk.Checkbutton(tela, text="check box", variable=var, onvalue="On", offvalue="Off")
chk_button.deselect()  
chk_button.pack()

tk.Button(tela, text="Show Me", command=show).pack()

txt_nome = tk.Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_nome.pack()
txt_nome.insert(0, "Digite o nome")

txt_idade = tk.Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_idade.pack()
txt_idade.insert(0, "Digite a idade")

txt_telefone = tk.Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_telefone.pack()
txt_telefone.insert(0, "Digite o telefone")

txt_grau = tk.Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_grau.pack()
txt_grau.insert(0, "Digite o grau de parentesco")

txt_cidade = tk.Entry(tela, width=20, borderwidth=5, fg="blue", bg="white")
txt_cidade.pack()
txt_cidade.insert(0, "Digite a cidade")


def meu_click():
    lbl_cn = tk.Label(tela, text=txt_nome.get())
    lbl_cn.pack()

    lbl_ci = tk.Label(tela, text=txt_idade.get())
    lbl_ci.pack()
    
    lbl_ct = tk.Label(tela, text=txt_telefone.get())
    lbl_ct.pack()

    lbl_cg = tk.Label(tela, text=txt_grau.get())
    lbl_cg.pack()

    lbl_cc = tk.Label(tela, text=txt_cidade.get())
    lbl_cc.pack()

def cadastrar_familiar():
    nome = txt_nome.get()
    idade = txt_idade.get()
    idade = txt_idade.get()
    idade = txt_idade.get()
    idade = txt_idade.get()

btn_botao = tk.Button(tela, text="Click", command=meu_click)
btn_botao.pack()

def escolher_imagem():
    caminho_imagem = filedialog.askopenfilename(initialdir=pasta_inicial, title="Escolha uma imagem", filetypes=(("Arquivos de imagem", "*jpg;*.jpeg;*.png"),("Todos os arquivos", "*.*")))
    

    imagem_pill = Image.open(caminho_imagem)
    largura, altura = imagem_pill.size

    if largura > 150:
        proporcao = largura / 150
        nova_altura = int(altura / proporcao)
        imagem_pill = imagem_pill.resize((110, nova_altura))

    imagem_tk = ImageTk.PhotoImage(imagem_pill)
    lbl_imagem = tk.Label(tela, image=imagem_tk)
    lbl_imagem.image = imagem_tk
    lbl_imagem.place(x=10, y=50)
    
btn_escolher = Button(tela, text="Escolher imagem", command=escolher_imagem)
btn_escolher.place(x=10, y=140)

foto_salvar = tk.PhotoImage(file = r"icones/salvar.png")
foto_excluir = tk.PhotoImage(file = r"icones/excluir.png")
foto_alterar = tk.PhotoImage(file = r"icones/alterar.png")
foto_consultar = tk.PhotoImage(file = r"icones/consultar.png")
foto_sair = tk.PhotoImage(file = r"icones./sair.png")

btn_salvar = Button(tela, text="Salvar", image=foto_salvar, compound= tk.TOP).place(x=130,y=310)
btn_excluir = Button(tela, text="Excluir", image=foto_excluir, compound= tk.TOP).place(x=200,y=310)
btn_alterar = Button(tela, text="Alterar", image=foto_alterar, compound= tk.TOP).place(x=270,y=310)
btn_consultar = Button(tela, text="Consultar", image=foto_consultar, compound= tk.TOP).place(x=340,y=310)
btn_sair = Button(tela, text="Sair", image=foto_salvar, compound=tk.RIGHT).place(x=620,y=340)

tela.mainloop()

# Código assinado e de autoria de Paulo Seiji DSM 3