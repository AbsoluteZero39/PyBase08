from .operations import calc_obj
kak_to_tak=True
while kak_to_tak:
    try:
        stopp=''
        while stopp!='stop':
            first_num = float(input('first num = '))
            sec_num = float(input('second num = '))
            znak=input('vvedit znak + or - or / or *')
            command=input('stop? write stop to stop')
            try:
                if znak in calc_obj.keys() :
                    result=calc_obj[znak](first_num,sec_num)
                else:
                    print('такой операии нету')
            except ZeroDivisionError:
                print('it is not possible')
            if command=='stop':
                stopp='stop'
                kak_to_tak=False
            print('your result', result)
    except  ValueError:
        print('вы ввели не числа')
        first_num = float(input('first num = '))
        sec_num = float(input('second num = '))



