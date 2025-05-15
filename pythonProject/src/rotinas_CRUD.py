#CRUD em arquivos de texto

# CREATE - Criar 
with open("dados.txt", "w") as arquivo:
    arquivo.write("Linha 1\n")
    arquivo.write("Linha 2\n")
    arquivo.write("Linha 3\n")


# READ - Ler
with open("dados.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())


# UPDATE - Atualizar
# ler arquivo no armazenamento
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()


# Alterar arquivo
with open("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() == "Linha 2":
            arquivo.write("Linha 2 - Atualizada\n")
        else:
            arquivo.write(linha)


# DELETE - Deletar
# faz primeiro a leitura
with open("dados.txt", "r") as arquivo:
    linhas = arquivo.readlines()


# faz alteração
with open("dados.txt", "w") as arquivo:
    for linha in linhas:
        if linha.strip() != "Linha 2 - Atualizada":
            arquivo.write(linha)