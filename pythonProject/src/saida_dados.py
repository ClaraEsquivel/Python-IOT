#Formatação de saida de dados

nome = "Maria Joaquina"
idade = 16
peso = 50.0

print("Bem - vindo ao meu primeiro trampo")

#forma antiga
print("%s tem %d anos e pesa %.2f kg." % (nome, idade, peso))

#forma mais nova
print("{} tem {} anos e pesa {:.2f} kg.".format(nome, idade, peso))

#forma mais fácil
print(f"{nome} tem {idade} anos e pesa {peso:.2f} kg.")
