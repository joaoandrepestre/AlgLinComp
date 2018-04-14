# -*- coding: utf-8 -*-

import numbers


class Matriz:
    """Implementação da estrutura de dados matriz."""

    def __init__(self, mat):
        """Construtor da classe Matriz."""

        if not isinstance(mat, list):
            raise TypeError("Não é lista.")

        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError(
                    "Lista de listas não configura matriz (tamanho de linhas variável).")

        self.mat = mat
        self.col = len(mat[0])
        self.lin = len(mat)

    def __repr__(self):
        """Retorna uma representação em string da matriz."""

        resp = ""
        for i in range(self.lin):
            for j in range(self.col):
                resp += str(self.mat[i][j])
                if j < self.lin-1:
                    resp += " "
            resp += "\n"
        return resp

    def __add__(self, outro):
        """Retorna a soma das matrizes elemento a elemento."""

        if (self.col != outro.col) or (self.lin != outro.lin):
            raise Exception("Matrizes devem ter as mesmas dimensões.")

        resp = []
        for i in range(self.lin):
            resp.append([])
            for j in range(self.col):
                resp[i].append(self.mat[i][j] + outro.mat[i][j])

        return Matriz(resp)

    def __sub__(self, outro):
        """Retorna a diferença das matrizes elemento a elemento."""

        if (self.col != outro.col) or (self.lin != outro.lin):
            raise Exception("Matrizes devem ter as mesmas dimensões.")

        resp = []
        for i in range(self.lin):
            resp.append([])
            for j in range(self.col):
                resp[i].append(self.mat[i][j] - outro.mat[i][j])

        return Matriz(resp)

    def getLinha(self, linha):
        """Retorna a linha desejada como uma lista."""

        if (linha > self.lin):
            raise IndexError("A matriz não tem a linha desejada.")
        return self.mat[linha]

    def getColuna(self, coluna):
        """Retorna a coluna desejada como uma lista."""

        if (coluna > self.col):
            raise IndexError("A matriz não tem a coluna desejada.")
        resp = []
        for i in range(self.lin):
            resp.append(self.mat[i][coluna])
        return resp

    def __mul__(self, outro):
        """Se outro for numero, retorna o produto de cada elemento da matriz por outro.
           Se outro ofr matriz, retorna o produto matricial das matrizes."""

        if isinstance(outro, numbers.Number):
            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(self.mat[i][j] * outro)
            return Matriz(resp)

        elif isinstance(outro, Matriz):
            if (self.col != outro.lin):
                raise ValueError(
                    "Matrizes de tamanho incompatível para multiplicação.")

            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(
                        sum([x*y for (x, y) in zip(self.getLinha(i), outro.getColuna(j))]))
            return Matriz(resp)

        elif isinstance(outro, list):
            if(self.col != len(outro)):
                raise ValueError(
                    "Matriz e vetor de tamanho incompatível para multiplicação.")

            resp = []
            for i in range(self.lin):
                resp.append(0)
                for j in range(self.col):
                    resp[i] += self.mat[i][j]*outro[j]
            return resp

    def transposta(self):
        """Retorna a transposta da matriz"""

        resp = [[0 for i in range(self.lin)] for j in range(self.col)]
        for i in range(self.lin):
            for j in range(self.col):
                resp[j][i] = self.mat[i][j]

        return Matriz(resp)

    def maior_elemento_fora_diagonal(self,index=False):
        """Retorna o maior elemento fora da diagonal
        principal da matriz, ou seus índices."""

        maior = 10**(-10)
        maior_i = 0
        maior_j = 0
        for i in range(self.lin):
            for j in range(self.col):
                if i != j:
                    if abs(self.mat[i][j]) > maior:
                        maior = abs(self.mat[i][j])
                        maior_i=i
                        maior_j=j

        if(index):
            return (maior_i,maior_j)

        return maior
