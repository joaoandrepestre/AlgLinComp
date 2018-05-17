# -*- coding: utf-8 -*-

import math
from MatrizQuadrada import MatrizQuadrada
from GeradorDeMatriz import cria_matriz


class Funcao:
    """Conjunto de métodos para o cáculo de raízes de funções"""

    # Constantes
    TOL = 10**(-10)
    MAX = 10**(4)
    H = 10**(-10)
    Quad = {
        2:{
            "pontos": [-0.5773502691896257,0.5773502691896257],
            "pesos": [1.0,1.0]
        },

        3:{
            "pontos": [0.0,-0.7745966692414834,0.7745966692414834],
            "pesos": [0.8888888888888888,0.5555555555555556,0.5555555555555556]
        },

        4:{
            "pontos": [-0.3399810435848563,0.3399810435848563,-0.8611363115940526,0.8611363115940526],
            "pesos": [0.6521451548625461,0.6521451548625461,0.3478548451374538,0.3478548451374538]
        },

        5:{
            "pontos": [0.0,-0.5384693101056831,0.5384693101056831,-0.9061798459386640,0.9061798459386640],
            "pesos": [0.5688888888888889,0.4786286704993665,0.4786286704993665,0.2369268850561891,0.2369268850561891]
        },

        6:{
            "pontos": [],
            "pesos": []
        },

        7:{
            "pontos": [],
            "pesos": []
        },

        8:{
            "pontos": [],
            "pesos": []
        },

        9:{
            "pontos": [],
            "pesos": []
        },

        10:{
            "pontos": [],
            "pesos": []
        },

        11:{
            "pontos": [],
            "pesos": []
        },

        12:{
            "pontos": [],
            "pesos": []
        },

        13:{
            "pontos": [],
            "pesos": []
        }
    }

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

    def integracao_polinomial(self, a, b, num):
        """Calcula a integral entre os pontos a e b com o numero de pontos determinado."""
        d = float(abs(b-a))/(num-1)

        pontos = [a+i*d for i in range(num)]
        A = cria_matriz([[pontos[j]**i for j in range(num)] for i in range(num)])
        C = [float(b**j-a**j)/j for j in range(1,num+1)]
        pesos = A.resolve(C)

        soma = 0
        for i in range(num):
            soma += self.funcao(pontos[i])*pesos[i]

        return soma

    def integracao_quadratura(self, a, b, num):
        """Calcula a integral entre os pontos a e b com o numero de pontos determinado."""

        pontos = self.Quad.get(num).get("pontos")
        pesos = self.Quad.get(num).get("pesos")

        soma = 0
        for  i in range(num):
            soma += self.funcao(0.5*(a+b+pontos[i]*abs(b-a)))*pesos[i]

        return soma


def f(x):
    return 2+x+2*x**2

func = Funcao(f)
print("Integração Quadratura: "+str(func.integracao_quadratura(1,3,5)))

""" def f(x):
    return x*x - 4*math.cos(x)


r = Funcao(f)

print("Bisseção: "+str(r.bissecao(0, 10)))
print("Newton: "+str(r.Newton(10)))
print("Secante: "+str(r.Newton_secante(10)))
print("Interpolação: "+str(r.interpolacao_inversa([3.0, 5.0, 10.0])))
 """