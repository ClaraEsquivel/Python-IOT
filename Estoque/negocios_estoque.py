#Método de negócios de estoque
def adionar_item():
    codigo = input("Digite o código do item: ") 
    descricao = input("Digite a descrição do item: ") 
    fabricante = input("Digite o fabricante do item: ") 
    preco = input("Digite o preço do item: ")

    with open("estoque.txt", "a") as arquivo:
        arquivo.write(f"{codigo},{descricao},{fabricante},{preco}\n")
    print("Item adicionado com sucesso!")


def listar_estoque():
    with open("estoque.txt", "r") as arquivo:
        for linha in arquivo:
            item = linha.strip().split(",")
            print(f"Código: {item[0]}, Descrição: {item[1]}, Fabricante: {item[2]}, Preço: {item[3]}")


def alterar_item():
    codigo = input("Digite o código do item que deseja alterar: ")

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] == codigo:
                novo_codigo = input("Digite o novo código do item: ")
                nova_descricao = input("Digite a nova descrição do item: ")
                novo_fabricante = input("Digite o novo fabricante do item: ")
                novo_preco = input("Digite o novo preço do item: ")
                arquivo.write(f"{novo_codigo},{nova_descricao},{novo_fabricante},{novo_preco}\n")
            else:
                arquivo.write(linha)    
                print("Item alterado com sucesso!")

def excluir_item():
    codigo = input("Digite o código do item que deseja excluir: ")

    with open("estoque.txt", "r") as arquivo:
        linhas = arquivo.readlines()

    with open("estoque.txt", "w") as arquivo:
        for linha in linhas:
            item = linha.strip().split(",")
            if item[0] != codigo:
                arquivo.write(linha)
    print("Item excluído com sucesso!")                        

