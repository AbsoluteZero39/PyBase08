from string import whitespace, punctuation
n=0
a=[]
b=[]
while n!='':
    n=input('vvedite stroku  :')
    d=n.upper()
    for i in whitespace:
        d=d.replace(i,' ')
    for q in punctuation:
        d=d.replace(q,' ')
    m=d.split()
    for k in set(m):
        a=m.count(k)
        b.append((k,a))
for s in b:
    print(s)

