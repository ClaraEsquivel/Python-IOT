# MANIPULÇÃO DE ARQUIVO

# # Gravar dados em um arquivo de texto
# arquivo = open("arquivo.txt", "w")
# for linha in range(1, 101):
#     arquivo.write(f"{linha}\n" )
# arquivo.close()

# ler dados de um arquivo de texto
arquivo = open("arquivo.txt", "r")
for linha in arquivo.readlines():
    linha = linha.strip()  # Remove espaços em branco e quebras de linha
    print(linha)
    arquivo.close()