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
            "pontos": [0.6612093864662645,-0.6612093864662645,-0.2386191860831969,0.2386191860831969,-0.9324695142031521,0.9324695142031521],
            "pesos": [0.3607615730481386,0.3607615730481386,0.4679139345726910,0.4679139345726910,0.1713244923791704,0.1713244923791704]
        },

        7:{
            "pontos": [0.0,0.4058451513773972,-0.4058451513773972,-0.7415311855993945,0.7415311855993945,-0.9491079123427585,0.9491079123427585],
            "pesos": [0.4179591836734694,0.3818300505051189,0.3818300505051189,0.2797053914892766,0.2797053914892766,0.1294849661688697,0.1294849661688697]
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

    def Euler(self, ti, tf, x0):
        """Resolve a EDO."""

        h = 0.1
        num = int(1 + (tf-ti)/h)
        x = [0 for i in range(num)]
        x[0] = x0
        t = ti
        for i in range(1,num):
            k = self.funcao(t,x[i-1])
            x[i] = x[i-1] + k*h
            t += h

        return x

    def Runge_Kutta2(self, ti, tf, x0):
        """Resolve a EDO."""

        h = 0.1
        num = int(1 + (tf-ti)/h)
        x = [0 for i in range(num)]
        x[0] = x0
        t = ti
        for i in range(1,num):
            k1 = self.funcao(t,x[i-1])
            k2 = self.funcao(t+h,x[i-1]+h*k1)
            x[i] = x[i-1] + 0.5*h*(k1+k2)
            t += h

        return x

    def Runge_Kutta4(self, ti, tf, x0):
        """Resolve a EDO."""

        h = 0.1
        num = int(1 + (tf-ti)/h)
        x = [0 for i in range(num)]
        x[0] = x0
        t = ti
        for i in range(1,num):
            k1 = self.funcao(t,x[i-1])
            k2 = self.funcao(t+0.5*h,x[i-1]+0.5*h*k1)
            k3 = self.funcao(t+0.5*h,x[i-1]+0.5*h*k2)
            k4 = self.funcao(t+h,x[i-1]+h*k3)
            x[i] = x[i-1] + h*(k1+2*k2+2*k3+k4)/6.0
            t += h

        return x

    def Taylor(self, ti, tf, x0, dx0):
        """Resolve a EDO de segunda ordem."""

        h = 0.1
        num = int(1 + (tf-ti)/h)
        x = [0 for i in range(num)]
        x[0] = x0
        t = ti
        dx = dx0
        for i in range(1, num):
            ddx = self.funcao(t,x[i-1],dx)
            x[i] = x[i-1] + dx*h + ddx*h*h*0.5
            dx = dx + ddx*h
            t += h

        return x

    def Runge_Kutta_Nystrom(self, ti, tf, x0, dx0):
        """Resolve a Edo de segunda ordem."""

        h = 0.1
        num = int(1 + (tf-ti)/h)
        x = [0 for i in range(num)]
        x[0] = x0
        t = ti
        dx = dx0
        for i in range(1, num):
            k1 = 0.5*h*self.funcao(t,x[i-1],dx)
            q = 0.5*h*(dx + 0.5*k1)
            k2 = 0.5*h*self.funcao(t+0.5*h,x[i-1]+q,dx+k1)
            k3 = 0.5*h*self.funcao(t+0.5*h,x[i-1]+q,dx+k2)
            l = h*(dx+k3)
            k4 = 0.5*h*self.funcao(t+h,x[i-1]+l,dx+2*k3)
            x[i] = x[i-1] + h*(dx + (k1+k2+k3)/3.0)
            dx = dx + (k1 + 2*k2 + 2*k3 + k4)/3.0
            t += h

        return x