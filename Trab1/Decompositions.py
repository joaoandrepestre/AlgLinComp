LU_ex = [
         [1, 2, 2],
         [4, 4, 2],
         [4, 6, 4]]

Cholesky_ex = [
               [1,0.2,0.4],
               [0.2,1,0.5],
               [0.4,0.5,1]]


def e_quadrada(matriz):
    linhas = len(matriz)
    if linhas != len(matriz[0]):
        return False
    return True


def auxiliar(matriz, lin, col):
    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    linhas = len(matriz)
    auxiliar = []
    for i in range (0, linhas-1):
        nova_linha = []
        for k in range (0, linhas-1):
            if (k != col):
                nova_linha.append(matriz[i][k])
        auxiliar.append(nova_linha)
    
    return auxiliar


#def determinante(matriz):
#    if not e_quadrada(matriz):
#        raise ValueError("A matriz deve ser quadrada")
#
#   if len(matriz) == 2:
#        determinante = matriz[0][0] + matriz[1][1] - matriz[0][1] - matriz[1][0] 
#        return determinante
#    else:
#        for k in range(0, len(matriz)-1):
#            determinante = matriz[0][k] * determinante(auxiliar(matriz, lin, col)) * ((-1)**k)
#            return determinante
#
#    return determinante


def LU(matriz):
    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    #if (determinante(matriz) == 0):
    #    raise ValueError("A matriz nao pode ser singular")
    
    linhas = len(matriz)

    for k in range(0, linhas-1):
        for i in range(k+1, linhas):
            matriz[i][k] = matriz[i][k]/matriz[k][k]
        for j in range(k+1, linhas):
            for i in range(k+1, linhas):
                matriz[i][j] = matriz[i][j] - matriz[i][k]*matriz[k][j]

    return matriz


def Cholesky(matriz):
    if not e_quadrada(matriz):
        raise ValueError("A matriz deve ser quadrada")

    # testar se determinante nao nulo
    # testar se simetrica positiva definida

    linhas = len(matriz)

    for i in range(1, linhas):
        soma = 0
        for k in range(1, i-1):
            soma += matriz[i][k]**2
        matriz[i][i] = (matriz[i][i] - soma)**(1/2)
        for j in range(i+1, linhas):
            soma = 0
            for k in range(1, i-1):
                soma += matriz[i][k]*matriz[j][k]
            matriz[j][i] = (1/matriz[i][i])*(matriz[i][j] - soma)

    return matriz

LU_output = LU(LU_ex)
Cholesky_output = Cholesky(Cholesky_ex)
