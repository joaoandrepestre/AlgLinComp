# -*- coding: utf-8 -*-

LU_ex = [
         [1, 2, 2],
         [4, 4, 2],
         [4, 6, 4]]

Cholesky_ex = [
               [1,0.2,0.4],
               [0.2,1,0.5],
               [0.4,0.5,1]]

Cholesky_ex2 = [
               [4,12,-16],
               [12,37,-43],
               [-16,-43,98]]


def e_quadrada(matriz):
    """Retorna true sse a matriz for quadrada"""

    linhas = len(matriz)
    if linhas != len(matriz[0]):
        return False
    return True

def e_simetrica(matriz):
    """Retorna true sse a matriz for simetrica"""

    for i in range (0,len(matriz)):
        for j in range (0,len(matriz)):
            if (matriz[i][j] != matriz[j][i]):
                return False
    return True


def auxiliar(matriz, lin, col):
    """Retorna uma cópia da matriz removendo a linha lin e a coluna col"""

    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    linhas = len(matriz)
    auxiliar = []
    for i in range (0, linhas):
        if (i != lin):
            nova_linha = []
            for k in range (0, linhas):
                if (k != col):
                    nova_linha.append(matriz[i][k])
            auxiliar.append(nova_linha)
    
    return auxiliar


def determinante(matriz):
    """Calcula e retorna o determinante da matriz"""

    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    if len(matriz) == 1: 
        return matriz[0][0]
    
    det  = 0
    for k in range (0, len(matriz)):
        det += matriz[0][k] * determinante(auxiliar(matriz, 0, k)) * ((-1)**(k))
    
    return det

def e_positiva_definida(matriz):
    """Retorna true sse a matriz for positiva definida"""

    linhas = len(matriz)

    if linhas == 1:
        return matriz[0][0]>0

    if (determinante(matriz) > 0) and e_positiva_definida(auxiliar(matriz,linhas-1,linhas-1)):
        return True
    
    return False


def LU(matriz):
    """Realiza a decomposição da matriz em matrizes triangular inferior e superior"""

    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    if (determinante(matriz) == 0):
        raise ValueError("A matriz não pode ser singular")
    
    linhas = len(matriz)

    ret = [[matriz[lin][col] for col in range(linhas)] for lin in range(linhas)]
    for k in range (0, linhas-1):
        for i in range (k+1, linhas):
            ret[i][k] = ret[i][k]/ret[k][k]
        for j in range (k+1, linhas):
            for i in range (k+1, linhas):
                ret[i][j] = ret[i][j] - ret[i][k]*ret[k][j]

    return ret


def Cholesky(matriz):#agora parece funcionar com erros de aproximação
    """Realiza a decomposição da matriz em uma matriz triangular inferior e sua transposta"""

    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    if (determinante(matriz) == 0):
        raise ValueError("A matriz não pode ser singular")

    if not e_simetrica(matriz):
        raise ValueError("A matriz deve ser simétrica")

    if not e_positiva_definida(matriz):
        raise ValueError("A matriz deve ser positiva definida")

    linhas = len(matriz)

    ret = [[0 for col in range(linhas)] for lin in range(linhas)]
    for col in range (linhas):
        soma = 0
        for k in range (col):
            soma += ret[col][k]**2
        ret[col][col] = (matriz[col][col] - soma)**0.5
        for lin in range (col+1, linhas):
            soma = 0
            for k in range (col):
                soma += ret[col][k]*ret[lin][k]
            ret[lin][col] = (matriz[col][lin] - soma)/ret[col][col] 

    return ret

LU_output = LU(LU_ex)
Cholesky_output = Cholesky(Cholesky_ex)
