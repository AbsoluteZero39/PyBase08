from string import whitespace, punctuation
n=0
a=[]
while n!='':
    n=input('vvedite stroku  :')
    d=n.upper()
    for i in whitespace:
        d=d.replace(i,' ')
    for q in punctuation:
        d=d.replace(q,' ')
    m=d.split()
    for i in m:
        a.append(i)
for v in set(a):
    print(v)
