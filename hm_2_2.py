a=float(input('a='))
b=float(input('b='))
k=0
a=abs(int(round(a)))
b=abs(int(round(b)))
if b>a:
    for i in range(a,b+1):
        k=k+i
    print(k)
    print(-k)
else:
    for i in range(b,a+1):
        k=k+i
    print(k)
    print(-k)
print('sum elementov ot a do b and if sum<0')

    
