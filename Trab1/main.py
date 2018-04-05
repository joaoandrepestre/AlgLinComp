# -*- coding: utf-8 -*-

from GeradorDeMatriz import cria_matriz
from Matriz import Matriz
from MatrizQuadrada import MatrizQuadrada


LU_ex = cria_matriz([[1, 2, 2],
                     [4, 4, 2],
                     [4, 6, 4]])

Cholesky_ex = cria_matriz([[5,-4,1,0],
                           [-4,6,-4,1],
                           [1,-4,6,-4],
                           [0,1,-4,5]])

A = cria_matriz([[16,9,8,7,6,5,4,3,2,1],
                 [9,17,9,8,7,6,5,4,3,2],
                 [8,9,18,9,8,7,6,5,4,3],
                 [7,8,9,19,9,8,7,6,5,4],
                 [6,7,8,9,18,9,8,7,6,5],
                 [5,6,7,8,9,17,9,8,7,6],
                 [4,5,6,7,8,9,16,9,8,7],
                 [3,4,5,6,7,8,9,15,9,8],
                 [2,3,4,5,6,7,8,9,14,9],
                 [1,2,3,4,5,6,7,8,9,13]])

B = [4,0,8,0,12,0,8,0,4,0]

(L,U) = A.LU(True)
print("A:\n"+str(A))
print("L:\n"+str(L))
print("U:\n"+str(U))
print("Prova Real:\n"+str(L*U))
y = L.substituicao_para_frente(B)
x = U.retro_substituicao(y)
print("Solução: " + str(x))

print('fim do programa')