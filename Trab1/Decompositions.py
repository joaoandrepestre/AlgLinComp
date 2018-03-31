# -*- coding: utf-8 -*-

LU_ex = [
         [1, 2, 2],
         [4, 4, 2],
         [4, 6, 4]]

Cholesky_ex = [
               [1,0.2,0.4],
               [0.2,1,0.5],
               [0.4,0.5,1]]


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

    for k in range (0, linhas-1):
        for i in range (k+1, linhas):
            matriz[i][k] = matriz[i][k]/matriz[k][k]
        for j in range (k+1, linhas):
            for i in range (k+1, linhas):
                matriz[i][j] = matriz[i][j] - matriz[i][k]*matriz[k][j]

    return matriz


def Cholesky(matriz): #por algum motivo essa função não está mudando a matriz em nada
    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    if (determinante(matriz) == 0):
        raise ValueError("A matriz não pode ser singular")

    if not e_simetrica(matriz):
        raise ValueError("A matriz deve ser simétrica")

    if not e_positiva_definida(matriz):
        raise ValueError("A matriz deve ser positiva definida")

    linhas = len(matriz)

    for i in range (0, linhas):
        soma = 0
        for k in range (0, i-1):
            soma += matriz[i][k]**2
        matriz[i][i] = (matriz[i][i] - soma)**(1/2)
        for j in range (i+1, linhas):
            soma = 0
            for k in range (0, i-1):
                soma += matriz[i][k]*matriz[j][k]
            matriz[j][i] = (1/matriz[i][i])*(matriz[i][j] - soma)

    return matriz

#LU_output = LU(LU_ex)
#Cholesky_output = Cholesky(Cholesky_ex)
