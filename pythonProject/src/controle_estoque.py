def menu():
    while True:
        print("\n= = Controle de Estoque = =")
        print("1. Adicionar produto")
        print("2. Listar produto")
        print("3. Alterar produto")
        print("4. Excluir produto")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            print("\n= = Adicionar Produto = =")
        elif opcao == '2':
            print("\n= = Listar Produto = =")
        elif opcao == '3':
            print("\n= = Alterar Produto = =")
        elif opcao == '4':
            print("\n= = Excluir Produto = =")
        elif opcao == '0':
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida! Tente novamente.")

menu()
            

     