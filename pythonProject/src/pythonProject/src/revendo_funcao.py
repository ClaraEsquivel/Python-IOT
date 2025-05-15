#TRABALHANDO COM FUNÇÕES

import random
import math
import datetime

# Criando uma função
def soma(x, y):
    resultado = x + y
    return resultado

def soma2(x, y):
    return x + y

print(soma(10, 20))
print(soma2(15, 40))
   
    
# funcao para raiz quadrada    
print(math.sqrt(25))


# função para número aleatório
print (random.randint(1, 100)) 


# função para data e hora
agora = (datetime.datetime.now())
print(agora)
print(agora.year)
print(agora.month)
print(agora.day)
print(agora.hour)
print(agora.minute)
print(agora.second)
print(agora.microsecond)
print(agora.strftime("%d/%m/%Y %H:%M:%S"))

