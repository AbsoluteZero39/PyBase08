n = int(input('n='))
u = 1
v = 1
k = 1
print('номер числа Фибоначчи ',n)
while k < n :
    k = k + 1
    t = u + v
    u = v
    v = t


print ('Результат', u)
