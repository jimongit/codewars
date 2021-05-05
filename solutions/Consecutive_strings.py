def longest_consec(strarr, k):
    if(k<=0 or k>len(strarr)):return ""
    res=mx([''.join(strarr[i:i+k]) for i in range(len(strarr))])
    return res

def mx(lst):
    m=''
    for i in lst:
        m=i if len(i)>len(m) else m
    return m