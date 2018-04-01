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
                raise ValueError("Lista de listas não configura matriz (tamanho de linhas variável).")
        
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
            if (self.col != outro.linha):
                raise ValueError("Matrizes de tamanho incompatível para multiplicação.")
            
            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(sum([i*j for (i, j) in zip(self.getLinha(i), outro.getColuna(j))]))
            return Matriz(resp)

    def transposta(self):
        """Retorna a transposta da matriz"""

        resp = [[0 for i in range(self.lin)] for j in range(self.col)]
        for i in range (self.lin):
            for j in range(self.col):
                resp[j][i] = self.mat[i][j]

        return Matriz(resp)


    

class MatrizQuadrada(Matriz):
    """Implementação especial da estrutura de dados matriz para matrizes quadradas."""

    def __init__(self, mat):
        """Construtor da classe MatrizQuadrada."""

        Matriz.__init__(self, mat)
        
        if self.col != self.lin:
            raise ValueError("A matriz não é quadrada.") 
        
        self.dim = self.col

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

    def determinante(self):
        """Calcula e retorna o determinante da matriz."""

        if self.dim == 1: 
            return self.mat[0][0]
        
        det = 0
        for k in range(0, self.dim):
            det += ((-1)**(k)) * self.mat[0][k] * self.auxiliar(0,k).determinante()
        
        return det

    def e_simetrica(self):
        """Retorna true sse a matriz for simetrica."""

        for i in range(self.dim):
            for j in range(self.dim):
                if (self.mat[i][j] != self.mat[j][i]):
                    return False
        return True
    
    def e_positiva_definida(self):
        """Retorna true sse a matriz for positiva definida."""

        if self.dim == 1:
            return self.mat[0][0]>0

        if (self.determinante() > 0) and self.auxiliar(self.dim-1,self.dim-1).e_positiva_definida():
            return True
        
        return False

    def e_triangular_inferior(self):
        """Retorna true sse a matriz for triangular inferior."""

        for i in range (self.dim):
            for j in range (i+1,self.dim):
                if self.mat[i][j] != 0:
                    return False
        return True

    def e_triangular_superior(self):
        """Retorna true sse a matriz for triangular superior."""

        for j in range (self.dim):
            for i in range (j+1, self.dim):
                if self.mat[i][j] != 0:
                    return False
        return True

    def transposta(self):
        """Retorna a transposta da matriz."""

        resp = Matriz.transposta(self)
        return MatrizQuadrada(resp.mat)

    def LU(self):
        """Realiza a decomposição da matriz em matrizes
         triangular inferior e superior."""

        if self.determinante() == 0:
            raise ValueError("A matriz não pode ser singular.")
        
        resp = [[self.mat[lin][col] for col in range(self.dim)] for lin in range(self.dim)]
        for k in range (self.dim-1):
            for i in range (k+1, self.dim):
                resp[i][k] = float(resp[i][k]/resp[k][k])
            for j in range (k+1, self.dim):
                for i in range (k+1, self.dim):
                    resp[i][j] = resp[i][j] - resp[i][k]*resp[k][j]

        return MatrizQuadrada(resp)

    def Cholesky(self):
        """Realiza a decomposição da matriz em uma matriz
         triangular inferior e sua transposta."""

        if (self.determinante() == 0):
            raise ValueError("A matriz não pode ser singular.")

        if not self.e_simetrica():
            raise ValueError("A matriz deve ser simétrica.")

        if not self.e_positiva_definida():
            raise ValueError("A matriz deve ser positiva definida.")

        resp = [[0 for col in range(self.dim)] for lin in range(self.dim)]
        for col in range (self.dim):
            soma = 0
            for k in range (col):
                soma += resp[col][k]**2
            resp[col][col] = (self.mat[col][col] - soma)**0.5
            for lin in range (col+1, self.dim):
                soma = 0
                for k in range (col):
                    soma += resp[col][k]*resp[lin][k]
                resp[lin][col] = float((self.mat[col][lin] - soma)/resp[col][col]) 

        return MatrizQuadrada(resp)

    def substituicao_para_frente(self, vetor):
        """Realiza a substituição para frente no sistema 
        com a matriz e o vetor e retorna o vetor solução."""

        if (len(vetor) != self.dim):
            raise Exception("A matriz e o vetor devem ter as mesmas dimensões")

        if not self.e_triangular_inferior():
            raise ValueError("A matriz deve ser triangular inferior")

        resp = [0 for i in range (self.dim)]
        resp[0] = float(vetor[0]/self.mat[0][0])
        for i in range (1,self.dim):
            soma = 0
            for j in range (i):
                soma += self.mat[i][j]*resp[j]
            resp[i] = float((vetor[i] - soma)/self.mat[i][i])

        return resp

    def retro_substituicao(self, vetor):
        """Realiza retro-substituição no sistema
         com a matriz e o vetor e retorna o vetor solução."""

        if (len(vetor) != self.dim):
            raise Exception("A matriz e o vetor devem ter as mesmas dimensões")

        if not self.e_triangular_superior():
            raise ValueError("A matriz deve ser triangular inferior")

        resp = [0 for i in range (self.dim)]
        resp[self.dim-1] = float(vetor[self.dim-1]/self.mat[self.dim-1][self.dim-1])
        for i in range (self.dim-2,-1,-1):
            soma = 0
            for j in range (i+1,self.dim):
                soma += self.mat[i][j]*resp[j]
            resp[i] = float((vetor[i] - soma)/self.mat[i][i])

        return resp


LU_ex = MatrizQuadrada([[1, 2, 2],
                        [4, 4, 2],
                        [4, 6, 4]])

Cholesky_ex = MatrizQuadrada([[1,0.2,0.4],
                              [0.2,1,0.5],
                              [0.4,0.5,1]])

LU_output = LU_ex.LU()
Cholesky_output = Cholesky_ex.Cholesky()

vetor = [0.6,-0.3,-0.6]

print "LU_ex:"
print(LU_ex)
print "LU_output:"
print(LU_output)

print "Cholesky_ex:"
print(Cholesky_ex)
print "Cholesky_output:"
print(Cholesky_output)

print('fim do programa')