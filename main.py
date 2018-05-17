# -*- coding: utf-8 -*-

""" from Matriz import Matriz
from MatrizQuadrada import MatrizQuadrada
from GeradorDeMatriz import cria_matriz """
import math
from Funcao import Funcao
from Sistemas import Sistemas, ajuste_curvas
import os

def f(x):
    return math.log(math.cosh(x*0.18286186)) -50

func = Funcao(f)

print("Bisseção: "+str(func.bissecao(0,1)))
print("Newton: "+str(func.Newton(10)))
print("Secante: "+str(func.Newton_secante(10)))
#print("Interpolação: "+str(func.interpolacao_inversa([0,1,1.5])))

def g(x):
    return 4*math.cos(x)-math.exp(2*x)

func = Funcao(g)

print("Bisseção: "+str(func.bissecao(0,1)))
print("Newton: "+str(func.Newton(10)))
print("Secante: "+str(func.Newton_secante(10)))
print("Interpolação: "+str(func.interpolacao_inversa([0,1,2])))

def f1(args):
    return 16*args[0]**4 + 16*args[1]**4 + args[2]**4 -16

def f2(args):
    return args[0]**2 + args[1]**2 + args[2]**2 -3

def f3(args):
    return args[0]**3 -args[1] +args[2] -1

s = Sistemas([f1,f2,f3],3)

print("Newton: "+str(s.Newton([1,2,3])))
print("Broyden: "+str(s.Broyden([1,2,3])))

def curva(ponto):
    def f(params):
        return params[0]+params[1]*ponto**(params[2])

    return f

print("Ajuste: "+str(ajuste_curvas(curva,[1,2,3],[1,2,9],[0,1,2])))

""" A = cria_matriz([[9, 5, 3, 1, 2, 1],
                 [5, 10, 5, 3, 1, 2],
                 [3, 5, 9, 5, 1, 2],
                 [1, 3, 5, 6, 1, 2],
                 [2, 1, 1, 1, 5, 3],
                 [1, 2, 2, 2, 3, 4]])

B = [10, 20, 30, 40, 30, 10]

print("A:\n"+str(A))
print("B:\n"+str(B))

input()
os.system('clear')

print("\nCholesky:\n")
(L, Lt) = A.Cholesky(True)
print("L:\n"+str(L))
print("Lt:\n"+str(Lt))
print("Prova Real:\n"+str(L*Lt))
y = L.substituicao_para_frente(B)
x = Lt.retro_substituicao(y)
print("Solução: " + str(x))

input()
os.system('clear')

print("\nLU:\n")
(L, U) = A.LU(True)
print("L:\n"+str(L))
print("U:\n"+str(U))
print("Prova Real:\n"+str(L*U))
y = L.substituicao_para_frente(B)
x = U.retro_substituicao(y)
print("Solução: " + str(x))

input()
os.system('clear')

print("\nPower Method:\n")
(a, v) = A.metodo_de_potencias()
print("Maior autovalor:\n"+str(a)+"\n\nAutovetor:\n"+str(v))
 
input()
os.system('clear')


print("\nMétodo de Jacobi:\n")
(a, v) = A.Jacobi()
print("Autovalores:\n"+str(a)+"\nAutovetores:\n"+str(v))

input()
os.system('clear')

print("Determinante: "+str(A.determinante_rigido()))

input()
os.system('clear')


def f1(x):
    return 1


def f2(x):
    return x

s = Sistemas([f1,f2],1)

reta = s.minimos_quadrados([(-2.7, 3.0), (-1.0, 4.6), (0.0, 6.0), (1.0, 7.5), (1.6, 8.5), (3.1, 9.5)])
print("y = "+str(reta[0])+" + "+str(reta[1])+"x") """

print('fim do programa')
