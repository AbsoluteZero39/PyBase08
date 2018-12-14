from string import whitespace, punctuation

def get_vocabluary(text):
    z=[]
    s=[]
    for i in whitespace:
        text=text.replace(i,' ')
    for q in punctuation:
        text=text.replace(q,' ')
    text=text.split()
    for m in set(text):
        z.append(m)
        print('Переведите на анлглийский данное слово снизу')
        print(m)
        h=input('введите перевод на Английский')
        s.append(h)
        result=dict(zip(z,s))
    return result

TEXT = """Всем привет
Имя
Фрукт
"""

vocabluary = get_vocabluary(TEXT)

for j in vocabluary.items():
    print(j)
