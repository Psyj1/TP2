from tkinter import *
from tkinter import ttk, messagebox
from db import pegar_colecao

colecao = pegar_colecao("locais")

tela = Tk()
tela.title("Controle de Locais Turísticos")
tela.geometry("900x600")
tela.configure(bg="#2E8B57") 

var_guia = StringVar()
var_guia.set("sim")

def inserir():
    try:
        codigo = txt_codigo.get()
        nome = txt_nome.get()
        cidade = txt_cidade.get()
        estado = cmb_estado.get()
        valor = txt_valor.get()
        guia = var_guia.get()
        
        doc = {
            "_id": int(codigo),
            "nome": nome,
            "cidade": cidade,
            "estado": estado,
            "valor": float(valor) if valor else 0,
            "guia": guia
        }
        
        colecao.insert_one(doc)
        messagebox.showinfo("Sucesso", "Local cadastrado!")
        limpar()
        consultar()
    except Exception as e:
        messagebox.showerror("Erro", f"Erro: {str(e)}")

def consultar():
    for w in frame_resultados.winfo_children():
        w.destroy()
    
    Label(frame_resultados, text="CÓD", font=("Arial", 9, "bold"), bg="lightgray", width=8).grid(row=0, column=0)
    Label(frame_resultados, text="NOME", font=("Arial", 9, "bold"), bg="lightgray", width=20).grid(row=0, column=1)
    Label(frame_resultados, text="CIDADE", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=2)
    Label(frame_resultados, text="ESTADO", font=("Arial", 9, "bold"), bg="lightgray", width=10).grid(row=0, column=3)
    Label(frame_resultados, text="VALOR R$", font=("Arial", 9, "bold"), bg="lightgray", width=12).grid(row=0, column=4)
    Label(frame_resultados, text="GUIA", font=("Arial", 9, "bold"), bg="lightgray", width=10).grid(row=0, column=5)
    Label(frame_resultados, text="AÇÕES", font=("Arial", 9, "bold"), bg="lightgray", width=15).grid(row=0, column=6)
    
    dados = list(colecao.find().sort("_id", 1))
    
    for i, doc in enumerate(dados, 1):
        Label(frame_resultados, text=str(doc["_id"]), bg="white", width=8).grid(row=i, column=0)
        Label(frame_resultados, text=doc.get("nome", ""), bg="white", width=20).grid(row=i, column=1)
        Label(frame_resultados, text=doc.get("cidade", ""), bg="white", width=15).grid(row=i, column=2)
        Label(frame_resultados, text=doc.get("estado", ""), bg="white", width=10).grid(row=i, column=3)
        Label(frame_resultados, text=f"R$ {doc.get('valor', 0):.2f}", bg="white", width=12).grid(row=i, column=4)
        
        guia = "Sim" if doc.get("guia") == "sim" else "Não"
        Label(frame_resultados, text=guia, bg="white", width=10).grid(row=i, column=5)
        
        f_btn = Frame(frame_resultados, bg="white")
        f_btn.grid(row=i, column=6)
        Button(f_btn, text="Editar", command=lambda d=doc: carregar(d), width=6).pack(side=LEFT, padx=1)
        Button(f_btn, text="Excluir", command=lambda id=doc["_id"]: excluir(id), width=6).pack(side=LEFT, padx=1)

def excluir(codigo):
    if messagebox.askyesno("Confirmar", "Excluir local?"):
        colecao.delete_one({"_id": codigo})
        consultar()

def carregar(doc):
    limpar()
    txt_codigo.insert(0, str(doc["_id"]))
    txt_nome.insert(0, doc.get("nome", ""))
    txt_cidade.insert(0, doc.get("cidade", ""))
    cmb_estado.set(doc.get("estado", ""))
    txt_valor.insert(0, str(doc.get("valor", "")))
    var_guia.set(doc.get("guia", "sim"))

def atualizar():
    try:
        codigo = txt_codigo.get()
        colecao.update_one(
            {"_id": int(codigo)},
            {"$set": {
                "nome": txt_nome.get(),
                "cidade": txt_cidade.get(),
                "estado": cmb_estado.get(),
                "valor": float(txt_valor.get()) if txt_valor.get() else 0,
                "guia": var_guia.get()
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
    txt_cidade.delete(0, END)
    cmb_estado.set("")
    txt_valor.delete(0, END)
    var_guia.set("sim")

frame_cad = LabelFrame(tela, text="Cadastro de Locais Turísticos", font=("Arial", 12, "bold"), padx=10, pady=10)
frame_cad.pack(padx=10, pady=5, fill="x")

Label(frame_cad, text="Código:", font=("Arial", 10)).grid(row=0, column=0, sticky="w", pady=2)
txt_codigo = Entry(frame_cad, width=10, font=("Arial", 10))
txt_codigo.grid(row=0, column=1, pady=2, padx=5)

Label(frame_cad, text="Nome Local:*", font=("Arial", 10)).grid(row=0, column=2, sticky="w", pady=2)
txt_nome = Entry(frame_cad, width=40, font=("Arial", 10))
txt_nome.grid(row=0, column=3, pady=2, padx=5, columnspan=3)

Label(frame_cad, text="Cidade:", font=("Arial", 10)).grid(row=1, column=0, sticky="w", pady=2)
txt_cidade = Entry(frame_cad, width=20, font=("Arial", 10))
txt_cidade.grid(row=1, column=1, pady=2, padx=5)

Label(frame_cad, text="Estado:", font=("Arial", 10)).grid(row=1, column=2, sticky="w", pady=2)
estados = ["AC", "AL", "AP", "AM", "BA", "CE", "DF", "ES", "GO", "MA", "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ", "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO"]
cmb_estado = ttk.Combobox(frame_cad, values=estados, width=10, font=("Arial", 10))
cmb_estado.grid(row=1, column=3, pady=2, padx=5)

Label(frame_cad, text="Valor Entrada R$:", font=("Arial", 10)).grid(row=1, column=4, sticky="w", pady=2)
txt_valor = Entry(frame_cad, width=12, font=("Arial", 10))
txt_valor.grid(row=1, column=5, pady=2, padx=5)

Label(frame_cad, text="Necessita Guia:", font=("Arial", 10)).grid(row=2, column=0, sticky="w", pady=2)
f_guia = Frame(frame_cad)
f_guia.grid(row=2, column=1, pady=2, padx=5, sticky="w", columnspan=3)
Radiobutton(f_guia, text="Sim", variable=var_guia, value="sim", font=("Arial", 9)).pack(side=LEFT)
Radiobutton(f_guia, text="Não", variable=var_guia, value="nao", font=("Arial", 9)).pack(side=LEFT)

f_btn = Frame(frame_cad)
f_btn.grid(row=3, column=0, columnspan=6, pady=10)

Button(f_btn, text="Inserir", command=inserir, bg="green", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Atualizar", command=atualizar, bg="blue", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Consultar", command=consultar, bg="orange", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)
Button(f_btn, text="Limpar", command=limpar, bg="gray", fg="white", font=("Arial", 10, "bold"), width=10).pack(side=LEFT, padx=5)

frame_res = LabelFrame(tela, text="Locais Turísticos Cadastrados", font=("Arial", 12, "bold"), padx=10, pady=10)
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