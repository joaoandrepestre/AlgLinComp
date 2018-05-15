# -*- coding: utf-8 -*-

import math


class Funcao:
    """Conjunto de métodos para o cáculo de raízes de funções"""

    # Constantes
    TOL = 10**(-10)
    MAX = 10**(4)
    H = 10**(-10)

    def __init__(self, f):
        self.funcao = f

    def derivada(self):
        """Retorna a derivada de f."""

        def df(x):
            return (self.funcao(x+self.H)-self.funcao(x))/self.H

        return df

    def bissecao(self, a, b):
        """Encontra uma raiz da função f entre a e b."""

        delta = abs(b-a)
        while delta > self.TOL:
            mid = (a+b)/2.0
            y = self.funcao(mid)
            if(y == 0):
                break
            if(y < 0):
                a = mid
            if(y > 0):
                b = mid
            delta = abs(b-a)

        return mid

    def Newton(self, x0):
        """Econtra uma raiz da função f."""

        df = self.derivada()
        for k in range(self.MAX):
            x1 = x0 - self.funcao(x0)/df(x0)
            erro = abs(x1-x0)
            if(erro < self.TOL):
                return x1
            x0 = x1

        raise ValueError("Não converge.")

    def Newton_secante(self, x0):
        """Encontra uma raiz da função f."""

        x1 = x0 + self.H
        y0 = self.funcao(x0)
        for k in range(self.MAX):
            y1 = self.funcao(x1)
            x2 = x1 - y1*(x1-x0)/(y1-y0)
            erro = abs(x2-x1)
            if(erro < self.H):
                return x2
            x0 = x1
            x1 = x2
            y0 = y1

        raise ValueError("Não converge.")

    def interpolacao_inversa(self, pontos):
        """Econtra uma raiz de f."""
        sorted(pontos)

        x0 = 10**(36)
        for k in range(self.MAX):
            y = [self.funcao(pontos[j]) for j in range(3)]
            x = (y[1]*y[2]*pontos[0])/((y[0]-y[1])*(y[0]-y[2])) +\
                (y[0]*y[2]*pontos[1])/((y[1]-y[0])*(y[1]-y[2])) +\
                (y[0]*y[1]*pontos[2])/((y[2]-y[0])*(y[2]-y[1]))
            erro = abs(x-x0)
            if(erro < self.TOL):
                return x

            i = y.index(max(y))
            pontos[i] = x
            sorted(pontos)
            x0 = x

        raise ValueError("Não converge.")


def f(x):
    return x*x - 4*math.cos(x)


r = Funcao(f)

print("Bisseção: "+str(r.bissecao(0, 10)))
print("Newton: "+str(r.Newton(10)))
print("Secante: "+str(r.Newton_secante(10)))
print("Interpolação: "+str(r.interpolacao_inversa([3.0, 5.0, 10.0])))
