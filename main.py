import numpy as np
import matplotlib.pyplot as plt
from sympy import *
init_printing()
x,y,X,f,xf,z = symbols('x y X f xf z') #define x, y e f como variáveis simbólicas.

no = 123456
print("Digite os coeficientes estequiométricos dos reagentes")
a = input("coeficiente estequiométrico de a:  ")
b = input("coeficiente estequimétrico de b:  ")
c = input("coeficiente estequimétrico de c:  ")

modelo = input("\nEscolha o modelo de lei de velocidade: Ordem zero (0), Primeira ordem(1), Segunda ordem(2) ou Terceira ordem(3):  ")
while modelo not in ["0", "1", "2", "3" ]:
#while modelo !="0" and modelo !="1" and modelo !="2" and modelo !="3":
    print("Erro! Tente novamente")
    modelo = input("\nEscolha o modelo de lei de velocidade: Ordem zero (0), Primeira ordem(1), Segunda ordem(2) ou Terceira ordem(3):  ")

estado = input ("Em qual estado a reação se processa?: Líquido(1) ou Gasoso(2):  ")

if(b!=0 and c!=0):
    variavel = input("Qual das variaveis a seguir você precisa descobrir?:\n"
                     "Digite o numero correspondente \n"
                     "Conversão(1)\n"
                     "Tempo de reação(2)\n"
                     ""
                     )

if(b ==0 and c!=0):
    NBo = 0
    variavel= input("Qual das variaveis a seguir você precisa descobrir?: \n" 
                    "Digite o numero correspondente \n"
                    "Conversão(1)\n"
                    "Tempo de reação(2)\n"
                    ""
                    )

if(b!=0 and c==0):
    NCo = 0
    variavel= input("Qual das variaveis a seguir você precisa descobrir?: \n"
                    "Conversão(1)\n"
                    "Tempo de reação(2)\n"
                    ""
                    )

if(b!=0 and c==0):
    NCo = 0
    variavel= input("Qual das variaveis a seguir você precisa descobrir?: \n"
                    "Conversão(1)\n"
                    "Tempo de reação(2)\n"
                    ""
                    )

if(b!=0 and c==0):
    NCo = 0
    variavel= input("Qual das variaveis a seguir você precisa descobrir?: \n"
                    "Conversão(1)\n"
                    "Tempo de reação(2)\n"
                    ""
                    )

if(b==0 and c==0):
    NBo = 0
    NCo = 0
    variavel= input("Qual das variaveis a seguir você precisa descobrir?: \n"
                    "Conversão(1)\n"
                    "Tempo de reação(2)\n"
                    ""
                    )

# if(variavel == 1):
#     repet = 1
#     while(repet == 1):
#         print("Digite as variáveis solicitadas a seguir com notação decimal,\n"
#               "(Ex: 2.4, 1.0) caso não possua alguma digite \"no\" ")
#         NAo = input("Digite o valor do Número de Mols inicial do Componente A (mols) ")
#         if(b!=0):
#             NBo = input("Digite o valor do Número de Mols inicial do Componente B(mols) ")
#             if(c!=0):
#                 NCo = input("Digite o valor do Número de Mols inicial do Componente C(mols) ")
#                 t = input("Digite o Tempo de Operação (min)")
#                 if(t == no):
#                     repet = input("Não existe dados suficientes para estimar o volume, deseja colocar\n"