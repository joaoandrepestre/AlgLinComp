# -*- coding: utf-8 -*-

import math
import matplotlib.pyplot as plt
from Funcao import Funcao
from Sistemas import Sistemas, ajuste_curvas
import os

def f(x):
    return math.log(math.cosh(x*0.18286186)) -50

func = Funcao(f)

print("f(x) = log(cosh(x*sqrt(gk))) - 50\n")
print("Bisseção: x = "+str(func.bissecao(640,650)))
print("Newton: x = "+str(func.Newton(640)))
print("Secante: x = "+str(func.Newton_secante(640)))
print("Interpolação: x = "+str(func.interpolacao_inversa([640,645,650])))

input()
os.system('clear')

def g(x):
    return 4*math.cos(x)-math.exp(2*x)

func = Funcao(g)

print("f(x) = 4cos(x) - e**(2x)\n")
print("Bisseção: x = "+str(func.bissecao(-1,1)))
print("Newton: x = "+str(func.Newton(10)))
print("Secante: x = "+str(func.Newton_secante(10)))
print("Interpolação: x = "+str(func.interpolacao_inversa([0,1,2])))

input()
os.system('clear')

def f1(args):
    return 16*args[0]**4 + 16*args[1]**4 + args[2]**4 -16

def f2(args):
    return args[0]**2 + args[1]**2 + args[2]**2 -3

def f3(args):
    return args[0]**3 -args[1] +args[2] -1

s = Sistemas([f1,f2,f3],3)
n = s.Newton([1,2,3])
b = s.Broyden([1,2,3])

print("""Sistema:\n
         16x**4 + 16y**4 + z**4 = 16
         x**2 + y**2 + z**2 = 3
         x**3 - y + z = 1\n""")
print("Newton: x = "+str(n[0])+" y = "+str(n[1])+" z = "+str(n[2]))
print("Broyden: x = "+str(b[0])+" y = "+str(b[1])+" z = "+str(b[2]))

input()
os.system('clear')

def g1(args):
    return 2*args[1] + args[0]**2 + 6*args[2]**2 -1

def g2(teta1):
    def ret(args):
        return 8*args[1]**3 + 6*args[1]*args[0]**2 + 36*args[1]*args[0]*args[2] + 108*args[1]*args[2]**2 - teta1
    return ret

def g3(teta2):
    def ret(args):
        return 60*args[1]**4 + 60*(args[1]**2)*args[0]**2 + 576*(args[1]**2)*args[0]*args[2] + 2232*(args[1]**2)*args[2]**2 + 252*(args[2]**2)*args[0]**2 + 1296*(args[2]**3)*args[0] + 3348*args[2]**4 + 24*(args[0]**3)*args[2] + 3*args[0] - teta2
    return ret

sa = Sistemas([g1,g2(0),g3(3)],3)
sb = Sistemas([g1,g2(0.75),g3(6.5)],3)
sc = Sistemas([g1,g2(0),g3(11.667)],3)

na = sa.Newton([1,2,3])
ba = sa.Broyden([1,0,0])

print("""Sistema:\n
         2c3 + c2**2 + 6c4**2 = 1
         8c3**3 + 6c3*c2**2 + 36c3*c2*c4 + 108c3*c4**2 = 0
         60c3**4 + 60(c3**2)*c2**2 + 576(c3**2)*c2*c4 + 2232(c3**2)*c4**2 + 252(c4**2)*c2**2 + 1296(c4**3)*c2 +
         + 3348c4**4 + 24(c2**3)*c4 + 3c2 = 3\n""")
print("Newton: c2 = "+str(na[0])+" c3 = "+str(na[1])+" c4 = "+str(na[2]))
print("Broyden: c2 = "+str(ba[0])+" c3 = "+str(ba[1])+" c4 = "+str(ba[2]))

input()
os.system('clear')

nb = sa.Newton([1,2,3])
bb = sa.Broyden([1,0,0])

print("""Sistema:\n
         2c3 + c2**2 + 6c4**2 = 1
         8c3**3 + 6c3*c2**2 + 36c3*c2*c4 + 108c3*c4**2 = 0.75
         60c3**4 + 60(c3**2)*c2**2 + 576(c3**2)*c2*c4 + 2232(c3**2)*c4**2 + 252(c4**2)*c2**2 + 1296(c4**3)*c2 +
         + 3348c4**4 + 24(c2**3)*c4 + 3c2 = 6.5\n""")
print("Newton: c2 = "+str(nb[0])+" c3 = "+str(nb[1])+" c4 = "+str(nb[2]))
print("Broyden: c2 = "+str(bb[0])+" c3 = "+str(bb[1])+" c4 = "+str(bb[2]))

input()
os.system('clear')

nc = sa.Newton([1,2,3])
bc = sa.Broyden([1,0,0])

print("""Sistema:\n
         2c3 + c2**2 + 6c4**2 = 1
         8c3**3 + 6c3*c2**2 + 36c3*c2*c4 + 108c3*c4**2 = 0
         60c3**4 + 60(c3**2)*c2**2 + 576(c3**2)*c2*c4 + 2232(c3**2)*c4**2 + 252(c4**2)*c2**2 + 1296(c4**3)*c2 +
         + 3348c4**4 + 24(c2**3)*c4 + 3c2 = 11.667\n""")
print("Newton: c2 = "+str(nc[0])+" c3 = "+str(nc[1])+" c4 = "+str(nc[2]))
print("Broyden: c2 = "+str(bc[0])+" c3 = "+str(bc[1])+" c4 = "+str(bc[2]))

input()
os.system('clear')

def curva(ponto):
    def f(params):
        return params[0]+params[1]*ponto**(params[2])

    return f

params = ajuste_curvas(curva,[1,2,3],[1,2,9],[0,1,2])
print("x:\t1\t2\t3\ny:\t1\t2\t9\n")
print("Ajuste: f(x) = "+str(params[0])+" + "+str(params[1])+"*x**"+str(params[2]))

def ajustada(x):
    return params[0]+params[1]*x**params[2]

x = [0.1*i for i in range(-10,10)]
y = [ajustada(x[i]) for i in range(20)]
plt.plot(x,y,'ro')
plt.ylabel('Curva Ajustada')
plt.show()

input()
os.system('clear')

def h(x):
    return math.exp(-0.5*x*x)/(2*math.pi)**0.5

func = Funcao(h)
print("f(x) = e**(-0.5*x**2)/sqrt(2pi)\n")
print("Integral 0-1:")
print("Polinomial: "+str(func.integracao_polinomial(0,1,5)))
print("Quadratura de Gauss: "+str(func.integracao_quadratura(0,1,7))+"\n")

print("Integral 0-5:")
print("Polinomial: "+str(func.integracao_polinomial(0,5,5)))
print("Quadratura de Gauss: "+str(func.integracao_quadratura(0,5,7))+"\n")

input()
os.system('clear')

def edo(t,y):
    return -2*t*y*y

func = Funcao(edo)
euler = func.Euler(0,2,1)
rk2 = func.Runge_Kutta2(0,2,1)
rk4 = func.Runge_Kutta4(0,2,1)

def solexata(t):
    return 1/(1+t*t)

t = [i*0.1 for i in range(21)]
plt.plot(t,euler,'ro')
plt.ylabel('Euler')
plt.show()

plt.plot(t,rk2,'ro')
plt.ylabel('R.K.2')
plt.show()

plt.plot(t,rk4,'ro')
plt.ylabel('R.K.4')
plt.show()

input()
os.system('clear')

def F(t):
    return 2*math.sin(0.5*t) + math.sin(2*0.5*t) + math.cos(3*0.5*t)

def edo2(t,y,dy):
    return F(t) - 0.2*dy - y

func = Funcao(edo2)
taylor = func.Taylor(0,100,0,0)
rkn = func.Runge_Kutta_Nystrom(0,100,0,0)

t = [0.1*i for i in range(1001)]

plt.plot(t,taylor,'ro')
plt.ylabel('Taylor')
plt.show()

plt.plot(t,rkn,'ro')
plt.ylabel('R.K.N')
plt.show()

print("Fim do programa.")