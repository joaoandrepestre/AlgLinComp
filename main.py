# -*- coding: utf-8 -*-

from Matriz import Matriz
from MatrizQuadrada import MatrizQuadrada
from GeradorDeMatriz import cria_matriz
from Sistemas import Sistemas
import os

A = cria_matriz([[9, 5, 3, 1, 2, 1],
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
print("y = "+str(reta[0])+" + "+str(reta[1])+"x")

print('fim do programa')
