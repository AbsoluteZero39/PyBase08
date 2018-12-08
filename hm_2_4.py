print('номер числа Фибоначчи ')
n=-10
u = 1
v = 1
k = 1
while n<0:
    n=int(input('n='))
    while k < n :
        k = k + 1
        t = u + v
        u = v
        v = t

print ('Результат', u)
