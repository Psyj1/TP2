from tkinter import *
from tkinter import ttk, messagebox
from db import pegar_colecao
import datetime

colecao = pegar_colecao("pessoas")

tela = Tk()
tela.title("Controle de Pessoas")
tela.geometry("900x650")

var_sexo = StringVar()
var_sexo.set("m")

def data_atual():
    return datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

def inserir():
    try:
        codigo = txt_codigo.get()
        nome = txt_nome.get()
        idade = txt_idade.get()
        sexo = var_sexo.get()
        altura = txt_altura.get()
        peso = txt_peso.get()
        cidade = cmb_cidade.get()
        data_nasc = txt_data_nasc.get()
        descricao = txt_descricao.get("1.0", END)
        
        doc = {
            "_id": int(codigo),
            "nome": nome,
            "idade": int(idade) if idade else 0,
            "sexo": sexo,
            "altura": float(altura) if altura else 0,
            "peso": float(peso) if peso else 0,
            "cidade": cidade,
            "data_nasc": data_nasc,
            "data_cad": data_atual(),
            "descricao": descricao
        }
        
        colecao.insert_one(doc)
        messagebox.showinfo("Sucesso", "Cadastrado!")
        limpar()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def consultar():
    for w in frame_resultados.winfo_children():
        w.destroy()
    
    Label(frame_resultados, text="CÓD", font=("Arial", 9, "bold"), bg="lightgray", width=8).grid(row=0, column=0)
    Label(frame_resultados, text="NOME", font=("Arial", 9, "bold"), bg="lightgray", width=20).grid(row=0, column=1)
    Label(frame_resultados, text="IDADE", font=("Arial", 9, "bold"), bg="lightgray", width=8).grid(row=0, column=2)
    Label(frame_resultados, text="SEXO", font=("Arial", 9, "bold"), bg="lightgray", width=8).grid(row=0, column=3)
    Label(frame_resultados, text="AÇÕES", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=4)
    
    dados = list(colecao.find().sort("_id", 1))
    
    for i, doc in enumerate(dados, 1):
        Label(frame_resultados, text=str(doc["_id"]), bg="white", width=8).grid(row=i, column=0)
        Label(frame_resultados, text=doc.get("nome", ""), bg="white", width=20).grid(row=i, column=1)
        Label(frame_resultados, text=str(doc.get("idade", "")), bg="white", width=8).grid(row=i, column=2)
        Label(frame_resultados, text=doc.get("sexo", ""), bg="white", width=8).grid(row=i, column=3)
        
        f_btn = Frame(frame_resultados, bg="white")
        f_btn.grid(row=i, column=4)
        Button(f_btn, text="Editar", command=lambda d=doc: carregar(d), width=6).pack(side=LEFT, padx=1)
        Button(f_btn, text="Excluir", command=lambda id=doc["_id"]: excluir(id), width=6).pack(side=LEFT, padx=1)

def excluir(codigo):
    if messagebox.askyesno("Confirmar", "Excluir?"):
        colecao.delete_one({"_id": codigo})
        consultar()

def carregar(doc):
    limpar()
    txt_codigo.insert(0, str(doc["_id"]))
    txt_nome.insert(0, doc.get("nome", ""))
    txt_idade.insert(0, str(doc.get("idade", "")))
    var_sexo.set(doc.get("sexo", "m"))
    txt_altura.insert(0, str(doc.get("altura", "")))
    txt_peso.insert(0, str(doc.get("peso", "")))
    cmb_cidade.set(doc.get("cidade", ""))
    txt_data_nasc.insert(0, doc.get("data_nasc", ""))
    txt_descricao.insert("1.0", doc.get("descricao", ""))

def atualizar():
    try:
        codigo = txt_codigo.get()
        colecao.update_one(
            {"_id": int(codigo)},
            {"$set": {
                "nome": txt_nome.get(),
                "idade": int(txt_idade.get()) if txt_idade.get() else 0,
                "sexo": var_sexo.get(),
                "altura": float(txt_altura.get()) if txt_altura.get() else 0,
                "peso": float(txt_peso.get()) if txt_peso.get() else 0,
                "cidade": cmb_cidade.get(),
                "data_nasc": txt_data_nasc.get(),
                "descricao": txt_descricao.get("1.0", END)
            }}
        )
        messagebox.showinfo("Sucesso", "Atualizado!")
        limpar()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def limpar():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_idade.delete(0, END)
    var_sexo.set("m")
    txt_altura.delete(0, END)
    txt_peso.delete(0, END)
    cmb_cidade.set("")
    txt_data_nasc.delete(0, END)
    txt_descricao.delete("1.0", END)

# INTERFACE (design anterior mantido)
frame_cad = LabelFrame(tela, text="Cadastro de Pessoas", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_cad.pack(padx=10, pady=5, fill="x")

Label(frame_cad, text="Código:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=2)
txt_codigo = Entry(frame_cad, width=10, font=("Arial", 10))
txt_codigo.grid(row=0, column=1, pady=2, padx=5)

Label(frame_cad, text="Nome:*", font=("Arial", 10)).grid(row=0, column=2, sticky="w", pady=2)
txt_nome = Entry(frame_cad, width=30, font=("Arial", 10))
txt_nome.grid(row=0, column=3, pady=2, padx=5)

Label(frame_cad, text="Idade:", font=("Arial", 10)).grid(row=0, column=4, sticky="w", pady=2)
txt_idade = Entry(frame_cad, width=10, font=("Arial", 10))
txt_idade.grid(row=0, column=5, pady=2, padx=5)

Label(frame_cad, text="Sexo:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=2)
f_sexo = Frame(frame_cad)
f_sexo.grid(row=1, column=1, pady=2, padx=5, sticky="w")
Radiobutton(f_sexo, text="Masculino", variable=var_sexo, value="m", font=("Arial", 9)).pack(side=LEFT)
Radiobutton(f_sexo, text="Feminino", variable=var_sexo, value="f", font=("Arial", 9)).pack(side=LEFT)

Label(frame_cad, text="Altura (m):", font=("Arial", 10)).grid(row=1, column=2, sticky="w", pady=2)
txt_altura = Entry(frame_cad, width=10, font=("Arial", 10))
txt_altura.grid(row=1, column=3, pady=2, padx=5)

Label(frame_cad, text="Peso (kg):", font=("Arial", 10)).grid(row=1, column=4, sticky="w", pady=2)
txt_peso = Entry(frame_cad, width=10, font=("Arial", 10))
txt_peso.grid(row=1, column=5, pady=2, padx=5)

Label(frame_cad, text="Cidade:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=2)
cidades = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Brasília", "Salvador", "Fortaleza", "Recife", "Porto Alegre", "Curitiba", "Manaus"]
cmb_cidade = ttk.Combobox(frame_cad, values=cidades, width=20, font=("Arial", 10))
cmb_cidade.grid(row=2, column=1, pady=2, padx=5, columnspan=2)

Label(frame_cad, text="Data Nasc.:", font=("Arial", 10)).grid(row=2, column=3, sticky="w", pady=2)
txt_data_nasc = Entry(frame_cad, width=15, font=("Arial", 10))
txt_data_nasc.grid(row=2, column=4, pady=2, padx=5)
Label(frame_cad, text="(dd/mm/aaaa)", font=("Arial", 8), fg="gray").grid(row=2, column=5, sticky="w", pady=2)

Label(frame_cad, text="Descrição:", font=("Arial", 10)).grid(row=3, column=0, sticky="nw", pady=2)
txt_descricao = Text(frame_cad, width=50, height=3, font=("Arial", 10))
txt_descricao.grid(row=3, column=1, pady=2, padx=5, columnspan=5, sticky="we")

f_btn = Frame(frame_cad)
f_btn.grid(row=4, column=0, columnspan=6, pady=10)

Button(f_btn, text="Inserir", command=inserir, bg="green", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Atualizar", command=atualizar, bg="blue", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Consultar", command=consultar, bg="orange", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Limpar", command=limpar, bg="gray", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)

frame_res = LabelFrame(tela, text="Registros Cadastrados", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_res.pack(padx=10, pady=5, fill="both", expand=True)

canvas = Canvas(frame_res)
scrollbar = ttk.Scrollbar(frame_res, orient="vertical", command=canvas.yview)
frame_resultados = Frame(canvas)

frame_resultados.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
canvas.create_window((0, 0), window=frame_resultados, anchor="nw")
canvas.configure(yscrollcommand=scrollbar.set)

canvas.pack(side="left", fill="both", expand=True)
scrollbar.pack(side="right", fill="y")

consultar()
tela.mainloop()