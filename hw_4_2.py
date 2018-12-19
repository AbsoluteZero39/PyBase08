import string

def clear_word(word, filterstr):
    for ii in word:
        if ii not in filterstr:
            word=word.replace(ii,' ')
    lenn=word.split()
    for ln in lenn:
        if len(ln)==1:
            del lenn[lenn.index(ln)]
    result1=lenn
    return result1

def get_eng_words(text):
    sttr=''
    for i in text:
        sttr=sttr+' '+i
    result=clear_word(sttr,string.ascii_letters)
        
    return result










a=["What is world?", "World is peace!", "В Data Science язык программирования Python\tнашёл широкое применение.", "непRавильные сл0ва сЦ1фрам - 123"]
result=get_eng_words(a)
print(result)
