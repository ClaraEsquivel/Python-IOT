#entreada de dados
"""
nome = input('Qual o seu nome? ')
idade = int (input('Qual a sua idade? '))
peso = float (input('Qual o seu peso? '))

print(f"{nome} tem {idade} anos e pesa {peso}kg")
"""


#colocar o valor  de uma variavel  dentro do input
nome = input('Qual o seu nome? ')
idade = int (input(f'Qual a idade de {nome}? '))
print(f"{nome} tem {idade} de idade")
