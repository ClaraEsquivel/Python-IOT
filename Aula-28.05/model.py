#salvar usuario e senha em um arquivo txt

from tkinter import messagebox

def salvar (usuario, senha):
    with open("dados.txt", "a") as arquivo:
        arquivo.write(f"{usuario}:{senha}\n")
        messagebox.showinfo("Sucesso", "Usuário e senha salvos com sucesso!")
    print("Usuário e senha salvos com sucesso!")    