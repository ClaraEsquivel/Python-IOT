#estruturas condicionais
from lib2to3.pgen2.token import NUMBER
"""
#verificar se o numero é positivo, negativo ou zero

num = int(input("Insira um número: "))
if num > 0:
    print("O numero é positivo")
elif num < 0:
    print("O numero é negativo")
else:
    print("O numero é zero")
"""

#verificar ano bissexto
ano = int(input("Insira um ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f"{ano} é bissexto")
else:
    print(f"{ano} não é bissexto")