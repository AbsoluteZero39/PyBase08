print('у нас есть квадратное уравнение a*x**2+b*x+c=0')
a=int(input('a= '))
b=int(input('b= '))
c=int(input('c= '))
discr=b**2 - 4*a*c
if a==0:
    x=(-c)/b
    print('if a=0',x)
else:
    if discr>0:
        print('2 вещественных корня')
        x1=(-b+discr**(1/2))/(2*a)
        x2=(-b-discr**(1/2))/(2*a)
        print(x1,'    ',x2)
    elif discr==0:
        print('1 вещ корень')
        x=(-b)/(2*a)
        print(x)
    elif discr<0:
        k=complex(discr)
        print(k)
        print('два комплексных корня')
        x1=(-b+k**(1/2))/(2*a)
        x2=(-b-k**(1/2))/(2*a)
        print(x1,'    ',x2)
    

    
