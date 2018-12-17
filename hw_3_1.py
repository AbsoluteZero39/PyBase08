from string import whitespace, punctuation
d=0
st=''
a=[]
b=[]
while d!='':
    d=input('vvedite stroku  :').lower()
    st=st+" "+d
    for i in whitespace:
        st=st.replace(i,' ')
    for q in punctuation:
        st=st.replace(q,' ')
    m=st.split()
for k in set(m):
    a=m.count(k)
    b.append({k:a})
for jj in b:
    print(jj)


