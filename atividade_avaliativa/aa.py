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

# Lista de familiares já cadastrados
familiares = [
    {"nome": "André", "idade": 50, "telefone": "1111-1111", "grau": "Pai", "cidade": "Iguape"},
    {"nome": "Nicolle", "idade": 47, "telefone": "2222-2222", "grau": "Mãe", "cidade": "Iguape"},
    {"nome": "Lucas", "idade": 22, "telefone": "3333-3333", "grau": "Primo", "cidade": "Registro"},
    {"nome": "João", "idade": 75, "telefone": "4444-4444", "grau": "Tio", "cidade": "Cajati"},
]

# Função para verificar se é maior de idade
def maior_idade(idade):
    if idade >= 18:
        return "Maior de idade"
    else:
        return "Menor de idade"

# Função para exibir os familiares na tela
def exibir_familiares():
    lbl_resultado.config(text="")  # Limpa antes
    texto = ""
    for f in familiares:
        status = maior_idade(f["idade"])
        texto += f"{f['nome']} | Idade: {f['idade']} ({status}) | Telefone: {f['telefone']} | Grau: {f['grau']} | Cidade: {f['cidade']}\n"
    lbl_resultado.config(text=texto)

# Função para cadastrar novo familiar
def cadastrar():
    nome = entrada_nome.get()
    idade = entrada_idade.get()
    telefone = entrada_telefone.get()
    grau = entrada_grau.get()
    cidade = entrada_cidade.get()

    if nome == "" or idade == "":
        return  # Não faz nada se estiver vazio

    try:
        idade = int(idade)
    except ValueError:
        return  # Não faz nada se idade for inválida

    novo = {
        "nome": nome,
        "idade": idade,
        "telefone": telefone,
        "grau": grau,
        "cidade": cidade
    }

    familiares.append(novo)
    exibir_familiares()

# Janela principal
janela = tk.Tk()
janela.title("Cadastro de Familiares")
janela.geometry("600x500")

# Campos
tk.Label(janela, text="Nome").pack()
entrada_nome = tk.Entry(janela)
entrada_nome.pack()

tk.Label(janela, text="Idade").pack()
entrada_idade = tk.Entry(janela)
entrada_idade.pack()

tk.Label(janela, text="Telefone").pack()
entrada_telefone = tk.Entry(janela)
entrada_telefone.pack()

tk.Label(janela, text="Grau de parentesco").pack()
entrada_grau = tk.Entry(janela)
entrada_grau.pack()

tk.Label(janela, text="Cidade").pack()
entrada_cidade = tk.Entry(janela)
entrada_cidade.pack()

# Botão de cadastro
btn_cadastrar = tk.Button(janela, text="Cadastrar", command=cadastrar)
btn_cadastrar.pack(pady=10)

# Label para exibir familiares
lbl_resultado = tk.Label(janela, text="", justify="left", anchor="w")
lbl_resultado.pack()

# Mostrar familiares já cadastrados
exibir_familiares()

janela.mainloop()

# Código assinado e de autoria de Paulo Seiji DSM 3