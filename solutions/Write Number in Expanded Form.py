def expanded_form(n):
    str_n =str(n)
    res=''
    x=len(str_n)-1
    for i in range(len(str_n)):
        if (str_n[i]!='0'):
            zeros='0'*(x-i)
            tmp=f' + {str_n[i]}{zeros}'
            res+=f'{str_n[i]}{zeros}' if i==0 else tmp
    return res