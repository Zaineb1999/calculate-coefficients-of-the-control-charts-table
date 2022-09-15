import math


def f(x):
    return math.exp(-x*x)


def phi(x):
    i=0
    s=0
    xi=-10000
    while xi<=x:
        s=s+f(xi)
        xi=xi+(0.1)
        i=i+1
    return s*(0.1)


def d2(n):  # To calculate d2 coefficient
    s=0
    i=0
    xi=-10000
    while xi<=10000:
        s=s+xi*f(xi)*math.pow(phi(xi),n-1)
        xi=xi+(0.1)
        i=i+1
    return 2*n*s*(0.1)



def integralx(n,y,d2):
    s=0
    i=0
    xi=-10000
    r=math.pow(y-d2,2)
    while xi<=10000:
        m=phi(xi+y)-phi(xi)
        s=s+r*math.pow(m,n-2)*f(xi)*f(xi+y)
        xi=xi+(0.1)
        i=i+1
    return s*(0.1)


def d3(n,d2): # To calculate d3 coefficient
    s=0
    i=0
    yi=0
    while yi<=10000:
        s=s+integralx(n,yi,d2)
        yi=yi+(0.1)
        i=i+1
    return math.sqrt(n*(n-1)*s*(0.1))


def C4(n):  # To calculate C4 coefficient
    r=2/(n-1)
    t=math.gamma(n/2)
    p=math.gamma((n-1)/2)
    return math.sqrt(r)*t*p


def A2(d2,n): # To calculate A2 coefficient
    return 3/(d2*math.sqrt(n))


def A3(C4,n): # To calculate A3 coefficient
    return 3/(C4*math.sqrt(n))


def B3(C4):  # To calculate C4 coefficient
    t=C4*C4
    r=math.sqrt(1-t)
    return 1-(3*r/C4)


def B4(C4):  # To calculate B4 coefficient
    t=C4*C4
    r=math.sqrt(1-t)
    return 1+(3*r/C4)


def D3(d3,d2):  # To calculate D3 coefficient
    r=math.sqrt(d3)
    return 1-(3*r/d2)


def D4(d3,d2):  # To calculate D4 coefficient
    r=math.sqrt(d3)
    return 1+(3*r/d2)

