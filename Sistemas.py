# -*- coding: utf-8 -*-

import math
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

    def Jacob_iterativo(self, B, Y, deltax):
        """Recalcula a matriz Jacobiana."""

        bx = B*deltax
        ybx = [Y[j]-bx[j] for j in range(self.dim)]
        num = [[ybx[i]*deltax[j] for j in range(self.dim)] for i in range(self.dim)]
        num = cria_matriz(num)
        den = 1.0/sum([deltax[j]*deltax[j] for j in range(self.dim)])
        return B + num*den

    def Newton(self, x0):
        """Retorna o vetor solução para o sistema."""

        for k in range(self.MAX):
            J = self.Jacobiano(x0)
            J = J*(-1)
            J = cria_matriz(J.mat)
            F = [self.funcoes[j](x0) for j in range(len(self.funcoes))]
            deltax = J.resolve(F)
            x1 = [x0[j]+deltax[j] for j in range(self.dim)]
            erro = self.norma(deltax)/self.norma(x1)
            if(erro < self.TOL):
                return x1
            x0 = x1

        print("Não converge.")

    def Broyden(self, x0):
        """Retorna o vetor solução para o sistema."""

        B = self.Jacobiano(x0)
        for k in range(self.MAX):
            J = B*(-1)
            J = cria_matriz(J.mat)
            F0 = [self.funcoes[j](x0) for j in range(len(self.funcoes))]
            deltax = J.resolve(F0)
            x1 = [x0[j]+deltax[j] for j in range(self.dim)]
            erro = self.norma(deltax)/self.norma(x1)
            if(erro < self.TOL):
                return x1
            F1 = [self.funcoes[j](x1) for j in range(len(self.funcoes))]
            Y = [F1[j]-F0[j] for j in range(self.dim)]
            B = self.Jacob_iterativo(B,Y,deltax)
            x0 = x1

        print("Não converge.")


def ajuste_curvas(curva, x, y, params0):
    """Retorna o vetor de parametros para a curva."""

    f = [curva(x[i]) for i in range(len(x))]
    s = Sistemas(f, len(params0))

    for k in range(s.MAX):
        J = s.Jacobiano(params0)
        Jt = J.transposta()
        A = Jt*J
        A = cria_matriz(A.mat)
        F = [f[j](params0)-y[j] for j in range(len(f))]
        B = Jt*(-1)*F
        deltaparams = A.resolve(B)
        params1 = [params0[j]+deltaparams[j] for j in range(s.dim)]
        erro = s.norma(deltaparams)/s.norma(params1)
        if(erro < s.TOL):
            return params1
        params0 = params1

    print("Não converge.")