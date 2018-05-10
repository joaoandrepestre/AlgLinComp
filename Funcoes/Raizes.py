# -*- coding: utf-8 -*-

import math
# Constantes
TOL = 10**(-10)
MAX = 10**(4)
H = 10**(-10)


def derivada(f):
    """Retorna a derivada de f."""

    def df(x):
        return (f(x+H)-f(x))/H

    return df


def bissecao(f, a, b):
    """Encontra uma raiz da função f entre a e b."""

    delta = abs(b-a)
    while delta > TOL:
        mid = (a+b)/2.0
        y = f(mid)
        if(y == 0):
            break
        if(y < 0):
            a = mid
        if(y > 0):
            b = mid
        delta = abs(b-a)

    return mid


def Newton(f, x0):
    """Econtra uma raiz da função f."""

    df = derivada(f)
    for k in range(MAX):
        x1 = x0 - f(x0)/df(x0)
        erro = abs(x1-x0)
        if(erro < TOL):
            return x1
        x0 = x1

    raise ValueError("Não converge.")


def Newton_secante(f, x0):
    """Encontra uma raiz da função f."""

    x1 = x0 + H
    y0 = f(x0)
    for k in range(MAX):
        y1 = f(x1)
        x2 = x1 - y1*(x1-x0)/(y1-y0)
        erro = abs(x2-x1)
        if(erro < H):
            return x2
        x0 = x1
        x1 = x2
        y0 = y1

    raise ValueError("Não converge.")


def interpolacao_inversa(f, pontos):
    """Econtra uma raiz de f."""
    sorted(pontos)

    x0 = 10**(36)
    for k in range(MAX):
        y = [f(pontos[j]) for j in range(3)]
        x = (y[1]*y[2]*pontos[0])/((y[0]-y[1])*(y[0]-y[2])) +\
            (y[0]*y[2]*pontos[1])/((y[1]-y[0])*(y[1]-y[2])) +\
            (y[0]*y[1]*pontos[2])/((y[2]-y[0])*(y[2]-y[1]))
        erro = abs(x-x0)
        if(erro < TOL):
            return x

        i = y.index(max(y))
        pontos[i] = x
        sorted(pontos)
        x0 = x

    raise ValueError("Não converge.")


def f(x):
    return x*x - 4*math.cos(x)


print("Bisseção: "+str(bissecao(f, 0, 10)))
print("Newton: "+str(Newton(f, 10)))
print("Secante: "+str(Newton_secante(f, 10)))
print("Interpolação: "+str(interpolacao_inversa(f, [3.0, 5.0, 10.0])))
