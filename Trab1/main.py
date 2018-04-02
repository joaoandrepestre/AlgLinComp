# -*- coding: utf-8 -*-

from GeradorDeMatriz import cria_matriz

LU_ex = cria_matriz([[1, 2, 2],
                     [4, 4, 2],
                     [4, 6, 4]])

Cholesky_ex = cria_matriz([[1,0.2,0.4],
                           [0.2,1,0.5],
                           [0.4,0.5,1]])

(L,U) = LU_ex.LU(True)
(Cholesky_L,Cholesky_U) = Cholesky_ex.Cholesky(True)

vetor = [0.6,-0.3,-0.6]

print "LU_ex:"
print(LU_ex)
print "L:"
print(L)
print "U:"
print(U)

print "Cholesky_ex:"
print(Cholesky_ex)
print "Cholesky_L:"
print(Cholesky_L)
print "Cholesky_U:"
print(Cholesky_U)

print('fim do programa')