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


exemplo = Matriz([[1, 2, 2],
                [4, 4, 2],
                [4, 6, 4]])

exemplo2 = Matriz([[1, 2, 2],
                [4, 4, 2],
                [1, 6, 4]])
print(exemplo * exemplo2)

print(exemplo)
print('fim do programa')