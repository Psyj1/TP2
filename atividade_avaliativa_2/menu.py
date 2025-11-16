from tkinter import *
import os
import subprocess
import sys

def get_project_root():
    """Encontra a raiz do projeto TP2"""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Sobe um nível para a pasta TP2 se estiver em atividade_avaliativa_2
    if current_dir.endswith('atividade_avaliativa_2'):
        return os.path.dirname(current_dir)  # Volta para TP2
    return current_dir

def executar_arquivo(nome_arquivo):
    """Executa arquivos Python da pasta atividade_avaliativa_2"""
    try:
        project_root = get_project_root()
        pasta_arquivos = os.path.join(project_root, "atividade_avaliativa_2")
        caminho_completo = os.path.join(pasta_arquivos, nome_arquivo)
        
        print(f"Tentando abrir: {caminho_completo}")  # Debug
        
        if os.path.exists(caminho_completo):
            subprocess.Popen([sys.executable, caminho_completo])
        else:
            print(f"Arquivo não encontrado: {caminho_completo}")
    except Exception as e:
        print(f"Erro ao executar {nome_arquivo}: {e}")

def abrir_pessoas():
    executar_arquivo("pessoas.py")

def abrir_veiculos():
    executar_arquivo("veiculos.py")

def abrir_locais():
    executar_arquivo("locais.py")

def sair():
    janela.destroy()
    executar_arquivo("login.py")

# Interface
janela = Tk()
janela.title("Menu Principal")
janela.geometry("600x200")

Label(janela, text="MENU PRINCIPAL", font=("Arial", 16, "bold")).pack(pady=20)

frame = Frame(janela)
frame.pack(pady=20)

Button(frame, text="Pessoas", command=abrir_pessoas, width=12, height=2).pack(side=LEFT, padx=10)
Button(frame, text="Veículos", command=abrir_veiculos, width=12, height=2).pack(side=LEFT, padx=10)
Button(frame, text="Locais", command=abrir_locais, width=12, height=2).pack(side=LEFT, padx=10)
Button(frame, text="Sair", command=sair, width=12, height=2).pack(side=LEFT, padx=10)

janela.mainloop()