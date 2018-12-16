from string import whitespace, punctuation

def get_vocabluary(text):
    z=[]
    s=[]
    for i in whitespace:
        text=text.replace(i,' ')
    for q in punctuation:
        text=text.replace(q,' ')
        text=text.upper()
    text=text.split()
    for m in set(text):
        z.append(m)
        print('Переведите на анлглийский данное слово снизу')
        print(m)
        h=input('введите перевод на Английский')
        if h.isalnum():
            s.append(h)
        else:
            print('вы ввели не то')
            h=input('введите перевод')
            s.append(h)
        result=dict(zip(z,s))
    return result
nn='\n'
TEXT = """Всем привет
Имя
Фрукт
"""

vocabluary = get_vocabluary(TEXT)
for j in vocabluary.items():
    print(j)
dictionary=''
for zz in vocabluary.values():
    dictionary=dictionary+' '+zz
def translate(text, dictionary):
    kk={text:dictionary}
    result=kk
    return result
for bb in nn:
    TEXT=TEXT.replace(nn,' ')
mm=translate(TEXT,dictionary)
print(mm)
