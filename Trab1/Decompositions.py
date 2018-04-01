# -*- coding: utf-8 -*-

class Matriz:
    def __init__(self, mat):
        if not isinstance(mat, list):
            raise TypeError("Não é lista") 
        
        for i in mat:
            if len(i) != len(mat[0]):
                raise ValueError("Lista de listas não configura matriz (tamanho de linhas variável)")
        
        self.mat = mat
        self.col = len(mat[0])
        self.lin = len(mat)

    def __repr__(self):
        for i in range(self.lin):
            for j in range(self.col):
                print(str(self.mat[i][j]), end=' ')
            print()
        return ('')
    
    def __add__(self, outro):
        if (self.col != outro.col) or (self.lin != outro.lin):
            raise Exception("Matrizes devem ter as mesmas linhas e colunas")
        
        resp = []
        for i in range(self.lin):
            resp.append([])
            for j in range(self.col):
                resp[i].append(self.mat[i][j] + outro.mat[i][j])
        
        return Matriz(resp)

    def __sub__(self, outro):
        if (self.col != outro.col) or (self.lin != outro.lin):
            raise Exception("Matrizes devem ter as mesmas linhas e colunas")
        
        resp = []
        for i in range(self.lin):
            resp.append([])
            for j in range(self.col):
                resp[i].append(self.mat[i][j] - outro.mat[i][j])
        
        return Matriz(resp)
    
    def getLinha(self, linha):
        if (linha > self.lin):
            raise IndexError("A matriz não tem a linha desejada")
        return self.mat[linha]
    
    def getColuna(self, coluna):
        if (coluna > self.col):
            raise IndexError("A matriz não tem a coluna desejada")
        resp = []
        for i in range(self.lin):
            resp.append(self.mat[i][coluna])
        return resp

    def __mul__(self, outro):
        if isinstance(outro, int):
            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(self.mat[i][j] * outro)
            return Matriz(resp)

        elif isinstance(outro, Matriz):
            if (self.col != outro.linha):
                raise ValueError("Matrizes de tamanho incompatível para multiplicação")
            
            resp = []
            for i in range(self.lin):
                resp.append([])
                for j in range(self.col):
                    resp[i].append(sum([i*j for (i, j) in zip(self.getLinha(i), outro.getColuna(j))]))
            return Matriz(resp)

    

class MatrizQuadrada(Matriz):
    def __init__(self, mat):
        Matriz.__init__(self, mat)
        self.dim = self.col

    def e_simetrica(self):
        """Retorna true sse a matriz for simetrica"""

        for i in range(self.dim):
            for j in range(self.dim):
                if (self.mat[i][j] != self.mat[j][i]):
                    return False
        return True
    
    def auxiliar(self, lin, col):
        """Retorna uma cópia da matriz removendo a linha lin e a coluna col"""

        auxiliar = []
        for i in range(self.dim):
            if (i != lin):
                nova_linha = []
                for k in range(self.dim):
                    if (k != col):
                        nova_linha.append(self.mat[i][k])
                auxiliar.append(nova_linha)
        
        return MatrizQuadrada(auxiliar)

    def determinante(self):
        """Calcula e retorna o determinante da matriz"""

        if self.dim == 1: 
            return self.mat[0][0]
        
        det = 0
        for k in range(0, self.dim):
            det += ((-1)**(k)) * self.mat[0][k] * self.auxiliar(0,k).determinante()
        
        return det
    
    def e_positiva_definida(self):
        # Não testada
        """Retorna true sse a matriz for positiva definida"""

        if self.dim == 1:
            return self.mat[0][0]>0

        if (self.determinante() > 0) and self.auxiliar(self.dim-1,self.dim-1).e_positiva_definida():
            return True
        
        return False
    
    def LU(self):
        """Realiza a decomposição da matriz em matrizes triangular inferior e superior"""

        if self.determinante() == 0:
            raise ValueError("A matriz não pode ser singular")
        
        ret = [[self.mat[lin][col] for col in range(self.dim)] for lin in range(self.dim)]
        for k in range (0, self.dim-1):
            for i in range (k+1, self.dim):
                ret[i][k] = ret[i][k]/ret[k][k]
            for j in range (k+1, self.dim):
                for i in range (k+1, self.dim):
                    ret[i][j] = ret[i][j] - ret[i][k]*ret[k][j]

        return MatrizQuadrada(ret)


    def Cholesky(self):#agora parece funcionar com erros de aproximação
        # Falta testes como OO
        """Realiza a decomposição da matriz em uma matriz triangular inferior e sua transposta"""

        if (self.determinante() == 0):
            raise ValueError("A matriz não pode ser singular")

        if not self.e_simetrica():
            raise ValueError("A matriz deve ser simétrica")

        if not self.e_positiva_definida():
            raise ValueError("A matriz deve ser positiva definida")

        ret = [[0 for col in range(self.dim)] for lin in range(self.dim)]
        for col in range (self.dim):
            soma = 0
            for k in range (col):
                soma += ret[col][k]**2
            ret[col][col] = (self.mat[col][col] - soma)**0.5
            for lin in range (col+1, self.dim):
                soma = 0
                for k in range (col):
                    soma += ret[col][k]*ret[lin][k]
                ret[lin][col] = (self.mat[col][lin] - soma)/ret[col][col] 

        return ret


exemplo = MatrizQuadrada([[1, 2, 2],
                          [2, 5, 2],
                          [2, 2, 1]])

print(exemplo.LU())

print(exemplo)
print('fim do programa')