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
        
        return cria_matriz(resp)

    def __sub__(self, outro):
        """Retorna a diferença das matrizes elemento a elemento."""

        if (self.col != outro.col) or (self.lin != outro.lin):
            raise Exception("Matrizes devem ter as mesmas dimensões.")
        
        resp = []
        for i in range(self.lin):
            resp.append([])
            for j in range(self.col):
                resp[i].append(self.mat[i][j] - outro.mat[i][j])
        
        return cria_matriz(resp)
    
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
            return cria_matriz(resp)

        elif isinstance(outro, Matriz):
            if (self.col != outro.linha):
                raise ValueError("Matrizes de tamanho incompatível para multiplicação.")
            
            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(sum([i*j for (i, j) in zip(self.getLinha(i), outro.getColuna(j))]))
            return cria_matriz(resp)

    def transposta(self):
        """Retorna a transposta da matriz"""

        resp = [[0 for i in range(self.lin)] for j in range(self.col)]
        for i in range (self.lin):
            for j in range(self.col):
                resp[j][i] = self.mat[i][j]

        return cria_matriz(resp)


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
        return cria_matriz(resp.mat)

    def __sub__(self, outro):
        """Retorna a soma das matrizes elemento a elemento."""
        
        resp = Matriz.__sub__(self, outro)
        return cria_matriz(resp.mat)
    
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
        
        return cria_matriz(auxiliar)

    def determinante(self):
        """Calcula e retorna o determinante da matriz."""

        if self.dim == 1: 
            return self.mat[0][0]
        
        det = 0
        for k in range(0, self.dim):
            det += ((-1)**(k)) * self.mat[0][k] * self.auxiliar(0,k).determinante()
        
        return det
    
    def e_positiva_definida(self):
        """Retorna true sse a matriz for positiva definida."""

        if self.dim == 1:
            return self.mat[0][0]>0

        if (self.determinante() > 0) and self.auxiliar(self.dim-1,self.dim-1).e_positiva_definida():
            return True
        
        return False

    def transposta(self):
        """Retorna a transposta da matriz."""

        resp = Matriz.transposta(self)
        return MatrizQuadrada(resp.mat,self.sim,self.tsup,self.tinf)

    def LU(self, separa=False):
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

        if separa:
            Ltmp = [[0 for j in range(self.dim)] for i in range(self.dim)]
            for i in range(self.dim):
                for j in range(i+1):
                    if i==j:
                        Ltmp[i][j] = 1
                    else:
                        Ltmp[i][j] = resp[i][j]
            Utmp = [[0 for j in range(self.dim)] for i in range(self.dim)]
            for i in range(self.dim):
                for j in range(i,self.dim):
                    Utmp[i][j] = resp[i][j]

            return (MatrizQuadrada(Ltmp,triang_inf=True),MatrizQuadrada(Utmp,triang_sup=True)) 

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

        L = MatrizQuadrada(resp,triang_inf=True)
        if separa:
            U = L.transposta()
            return (L,U) 

        return L

    def substituicao_para_frente(self, vetor):
        """Realiza a substituição para frente no sistema 
        com a matriz e o vetor e retorna o vetor solução."""

        if (len(vetor) != self.dim):
            raise Exception("A matriz e o vetor devem ter as mesmas dimensões")

        if not self.tinf:
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

        if not self.tsup():
            raise ValueError("A matriz deve ser triangular inferior")

        resp = [0 for i in range (self.dim)]
        resp[self.dim-1] = float(vetor[self.dim-1]/self.mat[self.dim-1][self.dim-1])
        for i in range (self.dim-2,-1,-1):
            soma = 0
            for j in range (i+1,self.dim):
                soma += self.mat[i][j]*resp[j]
            resp[i] = float((vetor[i] - soma)/self.mat[i][i])

        return resp

def e_quadrada(mat):
    """Retorna true sse mat for quadrada."""
    return len(mat)==len(mat[0])

def e_simetrica(mat):
    """Retorna true sse mat for simétrica."""

    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if (mat[i][j] != mat[j][i]):
                return False
    return True

def e_triangular_inferior(mat):
    """Retorna true sse mat for triangular inferior."""

    for i in range (len(mat)):
        for j in range(i+1,len(mat[0])):
            if mat[i][j] != 0:
                return False
    return True

def e_triangular_superior(mat):
    """Retorna true sse a matriz for triangular superior."""

    for j in range (len(mat)):
        for i in range (j+1, len(mat)):
            if mat[i][j] != 0:
                return False
    return True

def cria_matriz(mat):
    """Avalia mat e cria a matriz adequada às suas características."""

    if e_quadrada(mat):
        
        if e_simetrica(mat):
            return MatrizQuadrada(mat,simetrica=True)
        if e_triangular_inferior(mat):
            return MatrizQuadrada(mat,triang_inf=True)
        if e_triangular_superior(mat):
            return MatrizQuadrada(mat,triang_sup=True)

        return MatrizQuadrada(mat)    
    
    else:
        return Matriz(mat)

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