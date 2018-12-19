import string
def clear_word(word, filterstr):
    try:
        for ii in word:
            if ii in u:
                k=True
            else:
                m=word.index(ii)
                raise ValueError
        for i in filterstr:
            word=word.replace(i,'')
        result=word
        return result
    except ValueError:
        for i in filterstr:
            word=word.replace(i,'')
        result=word+'   '+'ложный символ-->'+' '+ii+' '+str(m)+'-'+'его позиция'
        return result

a=input('введите ваше слово')
b=input('введите не нужный символ')
u=string.ascii_letters + string.digits + string.punctuation + string.whitespace
x=clear_word(a,b)
print(x)

    
