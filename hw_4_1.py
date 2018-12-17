def clear_word(word, filterstr):
    for i in filterstr:
        word=word.replace(i,' ')
    result=word
    return result
try:
    a=input('введите ваше слово')
    b=input('введите не нужный символ')
    for i in a:
        if ord(i)>=65 and ord(i)<=122:
            k=True
        else:
            m=a.index(i)
            raise ValueError
    x=clear_word(a,b)
    print(x)
except ValueError:
    print(i,'- наш символ',m,'- индекс нашего неверного символа')
    print(x)
