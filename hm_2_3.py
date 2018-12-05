n = int(input('n= '))
p = 1
if n>=0:
    for i in range(1, n + 1):
        p = p * i
else:
    print('n<0, put another n')
print(n, '!=', p, sep='')
