import negocios_estoque

def menu():
    while True:
        print("\n= = Controle de Estoque = =")
        print("1. Adicionar produto")
        print("2. Listar produto")
        print("3. Alterar produto")
        print("4. Excluir produto")
        print("0. Sair")
        print("= = = = = = = = = = = = = =")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n= = Adicionar Produto = =")
            negocios_estoque.adionar_item()

        elif opcao == '2':
            print("\n= = Listar Produto = =")
            negocios_estoque.listar_estoque()

        elif opcao == '3':
            print("\n= = Alterar Produto = =")
            negocios_estoque.alterar_item()

        elif opcao == '4':
            print("\n= = Excluir Produto = =")
            negocios_estoque.excluir_item()
            
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
            

     