def pig_it(t):
    t=t.split()
    res=''
    for i in t:
        if (i.isalnum()):
            s=i[1:]
            res+=s + i[0] + 'ay' + ' '
        else:res+=i
    return res.rstrip()