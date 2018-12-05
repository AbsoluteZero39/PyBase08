a=float(input('a='))
b=float(input('b='))
k=0
if b>a:
    for i in range(int(round(a)),int(round(b))+1):
        k=k+i
    print(k)
else:
    for i in range(int(round(b)),int(round(a))+1):
        k=k+i
    print(k)
print('sum elementov ot a do b')
