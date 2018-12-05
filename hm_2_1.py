print('у нас есть квадратное уравнение a*x**2+b*x+c=0')
a=float(input('a= '))
b=float(input('b= '))
c=float(input('c= '))
discr=b**2 - 4*a*c
if discr>0:
    print('2 вещественных корня')
    x1=(-b+discr**(1/2))/(2*a)
    x2=(-b-discr**(1/2))/(2*a)
    print(x1,'    ',x2)
elif discr==0:
    print('1 вещ корень')
    x=(-b)/(2*a)
    print(x)
else:
    print('два комплексных корня')
    k=complex(discr)
    print(k)
    x1=(-b+k**(1/2))/(2*a)
    x2=(-b-k**(1/2))/(2*a)
    print(x1,'    ',x2)
    
