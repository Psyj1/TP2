from tkinter import *
from tkinter import ttk, messagebox
from db import pegar_colecao

colecao = pegar_colecao("veiculos")

tela = Tk()
tela.title("Controle de Veículos")
tela.geometry("900x600")
tela.configure(bg="#8FBC8F")

var_tipo = StringVar()
var_tipo.set("sim")

def inserir():
    try:
        codigo = txt_codigo.get()
        nome = txt_nome.get()
        placa = txt_placa.get()
        marca = cmb_marca.get()
        modelo = txt_modelo.get()
        utilitario = var_tipo.get()
        
        doc = {
            "_id": int(codigo),
            "nome": nome,
            "placa": placa.upper(),
            "marca": marca,
            "modelo": modelo,
            "utilitario": utilitario
        }
        
        colecao.insert_one(doc)
        messagebox.showinfo("Sucesso", "Veículo cadastrado!")
        limpar()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def consultar():
    for w in frame_resultados.winfo_children():
        w.destroy()
    
    Label(frame_resultados, text="CÓD", font=("Arial", 9, "bold"), bg="lightgray", width=8).grid(row=0, column=0)
    Label(frame_resultados, text="NOME", font=("Arial", 9, "bold"), bg="lightgray", width=20).grid(row=0, column=1)
    Label(frame_resultados, text="PLACA", font=("Arial", 9, "bold"), bg="lightgray", width=12).grid(row=0, column=2)
    Label(frame_resultados, text="MARCA", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=3)
    Label(frame_resultados, text="MODELO", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=4)
    Label(frame_resultados, text="TIPO", font=("Arial", 9, "bold"), bg="lightgray", width=12).grid(row=0, column=5)
    Label(frame_resultados, text="AÇÕES", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=6)
    
    dados = list(colecao.find().sort("_id", 1))
    
    for i, doc in enumerate(dados, 1):
        Label(frame_resultados, text=str(doc["_id"]), bg="white", width=8).grid(row=i, column=0)
        Label(frame_resultados, text=doc.get("nome", ""), bg="white", width=20).grid(row=i, column=1)
        Label(frame_resultados, text=doc.get("placa", ""), bg="white", width=12).grid(row=i, column=2)
        Label(frame_resultados, text=doc.get("marca", ""), bg="white", width=15).grid(row=i, column=3)
        Label(frame_resultados, text=doc.get("modelo", ""), bg="white", width=15).grid(row=i, column=4)
        
        tipo = "Utilitário" if doc.get("utilitario") == "sim" else "Normal"
        Label(frame_resultados, text=tipo, bg="white", width=12).grid(row=i, column=5)
        
        f_btn = Frame(frame_resultados, bg="white")
        f_btn.grid(row=i, column=6)
        Button(f_btn, text="Editar", command=lambda d=doc: carregar(d), width=6).pack(side=LEFT, padx=1)
        Button(f_btn, text="Excluir", command=lambda id=doc["_id"]: excluir(id), width=6).pack(side=LEFT, padx=1)

def excluir(codigo):
    if messagebox.askyesno("Confirmar", "Excluir veículo?"):
        colecao.delete_one({"_id": codigo})
        consultar()

def carregar(doc):
    limpar()
    txt_codigo.insert(0, str(doc["_id"]))
    txt_nome.insert(0, doc.get("nome", ""))
    txt_placa.insert(0, doc.get("placa", ""))
    cmb_marca.set(doc.get("marca", ""))
    txt_modelo.insert(0, doc.get("modelo", ""))
    var_tipo.set(doc.get("utilitario", "sim"))

def atualizar():
    try:
        codigo = txt_codigo.get()
        colecao.update_one(
            {"_id": int(codigo)},
            {"$set": {
                "nome": txt_nome.get(),
                "placa": txt_placa.get().upper(),
                "marca": cmb_marca.get(),
                "modelo": txt_modelo.get(),
                "utilitario": var_tipo.get()
            }}
        )
        messagebox.showinfo("Sucesso", "Dados atualizados!")
        limpar()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def limpar():
    txt_codigo.delete(0, END)
    txt_nome.delete(0, END)
    txt_placa.delete(0, END)
    cmb_marca.set("")
    txt_modelo.delete(0, END)
    var_tipo.set("sim")

frame_cad = LabelFrame(tela, text="Cadastro de Veículos", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_cad.pack(padx=10, pady=5, fill="x")

Label(frame_cad, text="Código:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=2)
txt_codigo = Entry(frame_cad, width=10, font=("Arial", 10))
txt_codigo.grid(row=0, column=1, pady=2, padx=5)

Label(frame_cad, text="Nome Veículo:*", font=("Arial", 10)).grid(row=0, column=2, sticky="w", pady=2)
txt_nome = Entry(frame_cad, width=30, font=("Arial", 10))
txt_nome.grid(row=0, column=3, pady=2, padx=5)

Label(frame_cad, text="Placa:", font=("Arial", 10)).grid(row=0, column=4, sticky="w", pady=2)
txt_placa = Entry(frame_cad, width=15, font=("Arial", 10))
txt_placa.grid(row=0, column=5, pady=2, padx=5)

Label(frame_cad, text="Marca:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=2)
marcas = ["Fiat", "Chevrolet", "Volkswagen", "Ford", "Renault", "Hyundai", "Toyota", "Honda", "Nissan", "Jeep"]
cmb_marca = ttk.Combobox(frame_cad, values=marcas, width=18, font=("Arial", 10))
cmb_marca.grid(row=1, column=1, pady=2, padx=5)

Label(frame_cad, text="Modelo:", font=("Arial", 10)).grid(row=1, column=2, sticky="w", pady=2)
txt_modelo = Entry(frame_cad, width=20, font=("Arial", 10))
txt_modelo.grid(row=1, column=3, pady=2, padx=5)

Label(frame_cad, text="Tipo:", font=("Arial", 10)).grid(row=1, column=4, sticky="w", pady=2)
f_tipo = Frame(frame_cad)
f_tipo.grid(row=1, column=5, pady=2, padx=5, sticky="w")
Radiobutton(f_tipo, text="Utilitário", variable=var_tipo, value="sim", font=("Arial", 9)).pack(side=LEFT)
Radiobutton(f_tipo, text="Não utilitário", variable=var_tipo, value="nao", font=("Arial", 9)).pack(side=LEFT)

f_btn = Frame(frame_cad)
f_btn.grid(row=2, column=0, columnspan=6, pady=10)

Button(f_btn, text="Inserir", command=inserir, bg="green", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Atualizar", command=atualizar, bg="blue", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Consultar", command=consultar, bg="orange", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Limpar", command=limpar, bg="gray", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)

frame_res = LabelFrame(tela, text="Veículos Cadastrados", font=("Arial", 12, "bold"), padx=10, pady=10)
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