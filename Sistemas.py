# -*- coding: utf-8 -*-

from Matriz import Matriz
from MatrizQuadrada import MatrizQuadrada
from GeradorDeMatriz import cria_matriz

class Sistemas:
    """Conjunto de métodos para solução de sistemas não lineares"""

    # constantes
    TOL = 10**(-10)
    MAX = 10**(4)
    H = 10**(-10)

    def __init__(self, funcoes, dim):
        """Construtor da classe Sistemas"""
        self.funcoes = funcoes
        self.dim = dim

    def norma(self, vetor):
        """Retorna a norma 2 do vetor"""

        ret = 0
        for i in range(len(vetor)):
            ret += vetor[i]*vetor[i]

        return ret**(0.5)

    def derivada_parcial(self, func_index, var_index):
        """Calcula a derivada parcial da função"""

        def df(args):
            dargs = [args[j] for j in range(len(args))]
            dargs[var_index] += self.H
            f = self.funcoes[func_index]
            return (f(dargs) - f(args))/self.H

        return df

    def minimos_quadrados(self, pontos):
        """Retorna os parametros b0 a bn que melhor ajusta
        o conjunto de funções ao conjunto de pontos"""

        N = len(pontos)
        M = len(self.funcoes)
        P = []
        for i in range(N):
            x = pontos[i][0]
            P.append([])
            for j in range(M):
                f = self.funcoes[j]
                P[i].append(f(x))
        P = Matriz(P)
        Pt = P.transposta()
        A = Pt*P
        A = cria_matriz(A.mat)

        y = [pontos[i][1] for i in range(N)]
        C = Pt*y

        resp = A.resolve(C)
        return resp

    def Jacobiano(self, pontos):
        """Retorna a matriz Jacobiana para a função com os pontos"""

        ret = []
        for i in range(len(self.funcoes)):
            ret.append([])
            for j in range(self.dim):
                df = self.derivada_parcial(i, j)
                ret[i].append(df(pontos))
        
        return cria_matriz(ret)

    def Newton(self):
        """Retorna o vetor solução para o sistema"""

        x0 = [j+2 for j in range(self.dim)]
        for k in range(self.MAX):
            J = self.Jacobiano(x0)
            F = [self.funcoes[j](x0) for j in range(len(self.funcoes))]
            deltax = J.resolve(F)
            x1 = [x0[j]+deltax[j] for j in range(self.dim)]
            erro = self.norma(deltax)/self.norma(x1)
            if(erro < self.TOL):
                return x1
            x0 = x1

        raise ValueError("Não converge.")


def f1(args):
    return args[0] + 2*args[1] - 2


def f2(args):
    return args[0]*args[0] + 4*args[1]*args[1] - 4


s = Sistemas([f1, f2], 2)

print("Newton: "+str(s.Newton()))
