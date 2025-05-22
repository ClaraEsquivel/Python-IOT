from tkinter import *
menu_inicial = Tk()
menu_inicial.title("Sistema de Controle de Estoque")
# menu_inicial.geometry("500x500") # Definindo o tamanho da janela
menu_inicial.geometry("400x400+500+100") # Definindo o tamanho e a posição da janela
menu_inicial.minsize(400, 400) # Definindo o tamanho mínimo da janela
menu_inicial.maxsize(600, 600) # Definindo o tamanho máximo da janela
menu_inicial.configure(bg="#7b659e") # Definindo a cor de fundo da janela
menu_inicial.configure(cursor="hand2") # Definindo o cursor da janela
menu_inicial.resizable(width=False, height=False) # Definindo se a janela pode ser redimensionada
# menu_inicial.state("iconic") # Definindo o estado inicial da janela
# menu_inicial.state("zoomed") # Definindo o estado inicial da janela
menu_inicial.iconbitmap("icone.ico") # Definindo o ícone da janela







menu_inicial.mainloop()