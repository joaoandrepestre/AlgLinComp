# -*- coding: utf-8 -*-

from classes.Matriz import Matriz
from classes.MatrizQuadrada import MatrizQuadrada
from classes.GeradorDeMatriz import cria_matriz
import os

def resolve(matriz, vetor):
    """Resolve o sistema por decomposição LU"""

    if not isinstance(matriz, MatrizQuadrada):
        raise ValueError("A matriz deve ser quadrada.")

    (L, U) = matriz.LU(True)
    resp = L.substituicao_para_frente(vetor)
    resp = U.retro_substituicao(resp)

    return resp


def minimos_quadrados(funcoes, pontos):
    """Retorna os parametros b0 a bn que melhor ajusta
    o conjunto de funções ao conjunto de pontos"""

    N = len(pontos)
    M = len(funcoes)
    P = []
    for i in range(N):
        x = pontos[i][0]
        P.append([])
        for j in range(M):
            f = funcoes[j]
            P[i].append(f(x))
    P = Matriz(P)
    Pt = P.transposta()
    A = Pt*P
    A = cria_matriz(A.mat)

    y = [pontos[i][1] for i in range(N)]
    C = Pt*y

    resp = resolve(A, C)
    return resp


print("Lista 1:\n")

A = cria_matriz([[16, 9, 8, 7, 6, 5, 4, 3, 2, 1],
                 [9, 17, 9, 8, 7, 6, 5, 4, 3, 2],
                 [8, 9, 18, 9, 8, 7, 6, 5, 4, 3],
                 [7, 8, 9, 19, 9, 8, 7, 6, 5, 4],
                 [6, 7, 8, 9, 18, 9, 8, 7, 6, 5],
                 [5, 6, 7, 8, 9, 17, 9, 8, 7, 6],
                 [4, 5, 6, 7, 8, 9, 16, 9, 8, 7],
                 [3, 4, 5, 6, 7, 8, 9, 15, 9, 8],
                 [2, 3, 4, 5, 6, 7, 8, 9, 14, 9],
                 [1, 2, 3, 4, 5, 6, 7, 8, 9, 13]])

B = [4, 0, 8, 0, 12, 0, 8, 0, 4, 0]

print("A:\n"+str(A))
print("B:\n"+str(B))

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

print("\nCholesky:\n")
(L, Lt) = A.Cholesky(True)
print("L:\n"+str(L))
print("Lt:\n"+str(Lt))
print("Prova Real:\n"+str(L*Lt))
y = L.substituicao_para_frente(B)
x = Lt.retro_substituicao(y)
print("Solução: " + str(x))

print("\n--------------------------------------------------\n")

input()
os.system('clear')

print("Lista 2:\n")

A = cria_matriz([[3.0, 2.0, 0.0],
                 [2.0, 3.0, -1.0],
                 [0.0, -1.0, 3.0]])

print("A:\n"+str(A))

print("\nPower Method:\n")
(a, v) = A.metodo_de_potencias()
print("Maior autovalor:\n"+str(a)+"\n\nAutovetor:\n"+str(v))

input()
os.system('clear')


print("\nMétodo de Jacobi:\n")
(a, v) = A.Jacobi()
print("Autovalores:\n"+str(a)+"\nAutovetores:\n"+str(v))

print("\n--------------------------------------------------\n")

input()
os.system('clear')

print("Lista 3:\n")


def f1(x):
    return 1


def f2(x):
    return x


reta = minimos_quadrados(
    [f1, f2], [(1.0, 1.0), (2.0, 2.5), (3.0, 3.5), (4.0, 4.3)])
print("y = "+str(reta[0])+" + "+str(reta[1])+"x")

print("\n--------------------------------------------------\n")
print('fim do programa')
