from sympy import laplace_transform ,exp,sin,cos,plot,inverse_laplace_transform
from sympy.abc import t,s,a
import time
def basic():
    ft = (exp((2*t)*(-1))-1)**2
    ft2 = sin(2*t)*cos(2*t)
    F = laplace_transform(ft,t,s)
    F2 = laplace_transform(ft2,t,s)
    print(F)
    print(F2)


def inverse():
    F = 280/(s**2+14*s+245)
    F2 = (-s**2+52*s+445)/(s**3+10*s**2+89)
    print("begin")
    t1 = time.time()
    #ft = inverse_laplace_transform(F,s,t)
    ft2 = inverse_laplace_transform(F2,s,t)
    #print(ft)
    t2= time.time()
    print(t2-t1)
    print(ft2)

#inverse()
#basic()
def il():
    F = (2*s**2+3*s-1)/((s**2-2*s+2)*(s-1))
    t1 = time.time()
    ft2 = inverse_laplace_transform(F,s,t)
    t2 = time.time()
    print(t2-t1)
    print(ft2)
il()
