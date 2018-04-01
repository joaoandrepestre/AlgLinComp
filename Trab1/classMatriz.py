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

    


exemplo = MatrizQuadrada([[1, 2, 2],
                          [2, 5, 2],
                          [2, 2, 1]])

print(exemplo.auxiliar(1,2))

print(exemplo)
print('fim do programa')