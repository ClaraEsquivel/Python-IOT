# Estrutura de dados de repetição

# # Loop controlado
# x = 1
# while x <= 10:
#     print(x)
#     x += 1 #(x = x + +1)


# # Loop infinito
# while True:
#     print(x)
    

# # Outro loop infinito
# x = 2
# while x == 2:   
#     print(x)


# # Tabuada de um número
# num = int(input("Digite um número para ver a tabuada: "))
# x = 1
# while x <= 10:
#     print(x * num)
#     x += 1


# # Tabuada com contador e acumulador
# n = 1 #contador
# soma = 0  #acumulador   
# while n <= 10:
#     num = int(input("Digite um número: "))
#     soma = soma + num
#     n += 1
#     print("A soma dos números é:", soma)


# # Interrupção de uma repetição
# x = 1
# while x <= 10:
#     if x == 5:
#         break
#     x = x + 1
#     print("O loop foi interrompido na interação:", x)


# # Interrupção de uma repetição 2
# x = 0
# while True:
#     num = int(input("Digite um número: "))
#     if num == 0:
#         break
#     x = x + num
# print(x)    


# # Estrutura de repetição for
# for i in range(1,6):
#     print(i)

# for char in "Python":
#     print(char)


# # Estrutura de repetição for com lista
# lista = [1, 2, 3, 4, 5]
# for i in lista:
#     print(i)


# # Estrutura de repetição for com string
# computador =  ['Monitor', 'Teclado', 'Mouse']
# for i in computador:
#     print(i)


# Ver tamanho da lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(len(lista))


# # Adicionar elementos na lista
# lista.append(10)
# print(lista)


# # Remover elementos da lista
# lista.remove(10)
# print(lista)


# # Remover elementos da lista
# lista.pop(0)
# print(lista)


# # Remover elementos da lista pelo indice
# del lista[2]
# print(lista)


#localizar elemnto especifico na lista
elemento = int(input("Digite um número: "))
if elemento in lista:
    print("O número {elemento} está na lista")
else:
    print("O número {elemento} não está na lista")