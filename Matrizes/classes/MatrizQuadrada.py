# -*- coding: utf-8 -*-

import math
from classes.Matriz import Matriz


class MatrizQuadrada(Matriz):
    """Implementação especial da estrutura de dados matriz para matrizes quadradas."""

    def __init__(self, mat, simetrica=False, triang_inf=False, triang_sup=False):
        """Construtor da classe MatrizQuadrada."""

        Matriz.__init__(self, mat)

        self.dim = self.col
        self.sim = simetrica
        self.tinf = triang_inf
        self.tsup = triang_sup

    def __add__(self, outro):
        """Retorna a soma das matrizes elemento a elemento."""

        resp = Matriz.__add__(self, outro)
        return MatrizQuadrada(resp.mat)

    def __sub__(self, outro):
        """Retorna a soma das matrizes elemento a elemento."""

        resp = Matriz.__sub__(self, outro)
        return MatrizQuadrada(resp.mat)

    def auxiliar(self, lin, col):
        """Retorna uma cópia da matriz removendo a linha lin e a coluna col."""

        auxiliar = []
        for i in range(self.dim):
            if (i != lin):
                nova_linha = []
                for j in range(self.dim):
                    if (j != col):
                        nova_linha.append(self.mat[i][j])
                auxiliar.append(nova_linha)

        return MatrizQuadrada(auxiliar)

    def determinante_rigido(self):
        """Calcula e retorna o determinante da matriz."""

        if self.dim == 1:
            return self.mat[0][0]

        det = 0
        for k in range(0, self.dim):
            det += ((-1)**(k)) * self.mat[0][k] * \
                self.auxiliar(0, k).determinante()

        return det

    def determinante(self):
        """Calcula e retorna uma aproximação do determinante da matriz"""
        U = self.LU()
        det = 1
        for i in range(self.dim):
            det *= U.mat[i][i]
        if abs(det) <= 10**(-10):
            return 0
        return det

    def e_positiva_definida(self):
        """Retorna true sse a matriz for positiva definida."""

        if self.dim == 1:
            return self.mat[0][0] > 0

        if (self.determinante() > 0) and self.auxiliar(self.dim-1, self.dim-1).e_positiva_definida():
            return True

        return False

    def transposta(self):
        """Retorna a transposta da matriz."""

        resp = Matriz.transposta(self)
        return MatrizQuadrada(resp.mat, self.sim, self.tsup, self.tinf)

    def LU(self, separa=False):
        """Realiza a decomposição da matriz em matrizes
         triangular inferior e superior."""

        resp = [[self.mat[lin][col]
                 for col in range(self.dim)] for lin in range(self.dim)]
        for k in range(self.dim-1):
            for i in range(k+1, self.dim):
                resp[i][k] = float(resp[i][k])/float(resp[k][k])
            for j in range(k+1, self.dim):
                for i in range(k+1, self.dim):
                    resp[i][j] = resp[i][j] - resp[i][k]*resp[k][j]

        det = 1
        for i in range(self.dim):
            det *= resp[i][i]

        if abs(det) <= 10**(-10):
            raise ValueError("A matriz não pode ser singular")

        if separa:
            Ltmp = [[resp[i][j]
                     for j in range(self.dim)] for i in range(self.dim)]
            for i in range(self.dim):
                for j in range(i, self.dim):
                    Ltmp[i][j] = float(i == j)
            for i in range(self.dim):
                for j in range(i):
                    resp[i][j] = 0.0

            return (MatrizQuadrada(Ltmp, triang_inf=True), MatrizQuadrada(resp, triang_sup=True))

        return MatrizQuadrada(resp)

    def Cholesky(self, separa=False):
        """Realiza a decomposição da matriz em uma matriz
         triangular inferior e sua transposta."""

        if (self.determinante() == 0):
            raise ValueError("A matriz não pode ser singular.")

        if not self.sim:
            raise ValueError("A matriz deve ser simétrica.")

        if not self.e_positiva_definida():
            raise ValueError("A matriz deve ser positiva definida.")

        resp = [[0.0 for col in range(self.dim)] for lin in range(self.dim)]
        for col in range(self.dim):
            soma = 0
            for k in range(col):
                soma += resp[col][k]**2
            resp[col][col] = (self.mat[col][col] - soma)**0.5
            for lin in range(col+1, self.dim):
                soma = 0
                for k in range(col):
                    soma += resp[col][k]*resp[lin][k]
                resp[lin][col] = float(
                    (self.mat[col][lin] - soma))/float(resp[col][col])

        L = MatrizQuadrada(resp, triang_inf=True)
        if separa:
            U = L.transposta()
            return (L, U)

        return L

    def metodo_de_potencias(self):
        """Calcula o maior autovalor(em valor absoluto)
        do problema e o correspondente autovetor."""

        autovetor = [1.0 for i in range(self.dim)]
        autovalor = 1

        erro = 1
        while erro > 10**(-10):
            tmp_vetor = self*autovetor
            tmp_valor = tmp_vetor[0]
            erro = float(abs(tmp_valor-autovalor))/float(abs(tmp_valor))
            autovetor = [float(tmp_vetor[i])/float(tmp_vetor[0])
                         for i in range(self.dim)]
            autovalor = tmp_valor

        return (autovalor, autovetor)

    def Jacobi(self):
        """Calcula a matriz X de autovetores ortogonais."""

        if not self.sim:
            raise ValueError("A matriz deve ser simétrica.")

        A = MatrizQuadrada([[self.mat[x][y] for y in range(self.dim)]
                            for x in range(self.dim)], self.sim, self.tinf, self.tsup)
        X = MatrizQuadrada([[float(x == y) for y in range(self.dim)]
                            for x in range(self.dim)], simetrica=True)

        (i, j) = A.maior_elemento_fora_diagonal(True)
        erro = A.mat[i][j]
        while erro >= 10**(-3):
            aii = A.mat[i][i]
            ajj = A.mat[j][j]
            aij = A.mat[i][j]
            phi = math.pi/4.0
            if aii != ajj:
                phi = 0.5*math.atan2(2*aij, aii-aij)
            P = [[float(x == y) for y in range(self.dim)]
                 for x in range(self.dim)]
            cos = math.cos(phi)
            sin = math.sin(phi)
            P[i][i] = cos
            P[i][j] = sin
            P[j][i] = -sin
            P[j][j] = cos
            P = MatrizQuadrada(P)
            Pt = P.transposta()
            A = Pt*A*P
            X = X*P
            (i, j) = A.maior_elemento_fora_diagonal(True)
            erro = abs(A.mat[i][j])

        return (A, X)

    def substituicao_para_frente(self, vetor):
        """Realiza a substituição para frente no sistema 
        com a matriz e o vetor e retorna o vetor solução."""

        if (len(vetor) != self.dim):
            raise Exception("A matriz e o vetor devem ter as mesmas dimensões")

        if not self.tinf:
            raise ValueError("A matriz deve ser triangular inferior")

        resp = [0 for i in range(self.dim)]
        resp[0] = float(vetor[0]/self.mat[0][0])
        for i in range(1, self.dim):
            soma = 0
            for j in range(i):
                soma += self.mat[i][j]*resp[j]
            resp[i] = float((vetor[i] - soma)/self.mat[i][i])

        return resp

    def retro_substituicao(self, vetor):
        """Realiza retro-substituição no sistema
         com a matriz e o vetor e retorna o vetor solução."""

        if (len(vetor) != self.dim):
            raise Exception("A matriz e o vetor devem ter as mesmas dimensões")

        if not self.tsup:
            raise ValueError("A matriz deve ser triangular inferior")

        resp = [0 for i in range(self.dim)]
        resp[self.dim-1] = float(vetor[self.dim-1] /
                                 self.mat[self.dim-1][self.dim-1])
        for i in range(self.dim-2, -1, -1):
            soma = 0
            for j in range(i+1, self.dim):
                soma += self.mat[i][j]*resp[j]
            resp[i] = float((vetor[i] - soma)/self.mat[i][i])

        return resp
