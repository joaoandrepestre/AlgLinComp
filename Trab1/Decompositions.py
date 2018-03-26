

A = [[1,2,2],[4,4,2],[4,6,4]]

def LU(matrix):

    N = len(matrix)

    if N != len(matrix[0]):

        print("A matriz deve ser quadrada")
        return matrix

    #testar se determinante não nulo

    for k in range(0, N-1):

        for i in range(k+1, N):

            matrix[i][k] = matrix[i][k]/matrix[k][k]

        for j in range(k+1, N):

            for i in range(k+1, N):

                matrix[i][j] = matrix[i][j] - matrix[i][k]*matrix[k][j]


    return matrix


def Cholesky(matrix):

    N = len(matrix)

    if N != len(matrix[0]):

        print("A matriz deve ser quadrada")
        return matrix

    #testar se determinante não nulo
    #testar se simétrica positiva definida

    for i in range(1, N):

        sum = 0
        for k in range(1, i-1):

            sum += matrix[i][k]**2

        matrix[i][i] = (matrix[i][i] - sum)**(1/2)

        for j in range(i+1, N):

            sum = 0
            for k in range(1, i-1):

                sum += matrix[i][k]*matrix[j][k]

            matrix[j][i] = (1/matrix[i][i])*(matrix[i][j] - sum)


    return matrix

