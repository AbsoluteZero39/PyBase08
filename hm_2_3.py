n = -10
p = 1
while n<0:
    print('vvedite n>0')
    n = int(input('n= '))
    for i in range(1, n + 1):
        p = p * i

print(n,'!=', p,sep='')
