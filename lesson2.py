n=int(input('n='))
k=0
b=0
z=1
h=1
a=''
m=''
while n>0:
    k=n%2
    n=n//2
    a= a+str(k)
print(a[::-1])
d=a[::-1]

#to the other way

for i in range(len(a)):
    t=int(d[-z])
    b=b+(t*2)**z
    z=z+1
    
print(b/2)                            
  

string=input('Введите число 1 :')
string1=input('Введите число 2 Ж')
print(float(string))
print(float(string1))


x=float(input('x='))
print(int(float(x)))
