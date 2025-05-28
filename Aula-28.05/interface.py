#interface usando o gridLay do tkinter

from tkinter import *
import model
from tkinter import messagebox

def sair():
    resposta = messagebox.askyesno("Sair", "Deseja realmente sair?")
    if resposta: 
        menu_inicial.destroy()


def guardar_usuario():
    usuario = txtUsuario.get()
    senha = txtSenha.get()
    model.salvar(usuario, senha)  # Chama a função do model para salvar os dados
    # print(usuario)
    # print(senha)


menu_inicial = Tk()
menu_inicial.title("Tela Login")
menu_inicial.geometry("400x300+500+150")
menu_inicial.resizable(False, False)

#Criação dos widgets

#Rotulos
label1 = Label(menu_inicial, text="Usuário", fg= "blue", font=("Arial", 12))
label1.grid(row=0, column=0, padx=10, pady=10, sticky=W)
label2 = Label(menu_inicial, text="Senha", fg= "blue", font=("Arial", 12))
label2.grid(row=1, column=0, padx=10, pady=10, sticky=W)

#Entradas
txtUsuario = Entry(menu_inicial, width=30, font=("Arial", 12))
txtUsuario.grid(row=0, column=1, padx=10, pady=10)
txtSenha = Entry(menu_inicial, width=30, font=("Arial", 12), show="*")
txtSenha.grid(row=1, column=1, padx=10, pady=10)

#Botões
btLogin = Button(menu_inicial, text="Entrar", width=10, font=("Arial", 12), bg="green", fg="white",command=guardar_usuario)
btLogin.grid(row=2, column=0, padx=10, pady=10, sticky=W)

btCancelar = Button(menu_inicial, text="Cancelar", width=10, font=("Arial", 12), bg="red", fg="white", command=sair)
btCancelar.grid(row=2, column=1, padx=10, pady=10, sticky=W)


menu_inicial.mainloop()
