def clear_word(word, filterstr):
    word=word.replace(filterstr,'')
    result=word
    return result
a=input('введите ваше слово')
b=input('введите не нужный символ')
for i in a:
    if ord(i)>=65 and ord(i)<=122:
        k=True
    else:
        m=a.index(i)
        raise ValueError(i,'- наш символ',m,'- индекс нашего неверного символа')
x=clear_word(a,b)
print(x)
