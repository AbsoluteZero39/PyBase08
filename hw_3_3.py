
n=0
a=[]
while n!='':
    n=input('vvedite stroku  :')
    d=n.upper()
    m=d.split()
    for i in m:
        a.append(i)
for v in set(a):
    print(v)
