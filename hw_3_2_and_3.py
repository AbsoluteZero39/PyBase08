print('Ex.N2')
n=0
a=[]
while n!='':
    n=input('vvedite stroku  :')
    d=n.upper()
    m=d.split()
    for i in m:
        a.append(i)
print('Слова в алфавитном порядке')
for k in sorted(a):
    print(k)
print('-----------')
print('Ex.N3')
for v in set(a):
    print(v)



            
                       

            
            

    
