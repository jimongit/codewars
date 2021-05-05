def spin_words(s):
    res=''
    s=s.split()
    for i in s:
        if(len(i)>=5):
            res+=reverse(i)
        else: res+=i
        res+=' '
    res=res.rstrip()
    return res


def reverse(s):
    x=len(s)-1
    res=''
    while(x>=0):
        res+=s[x]
        x-=1
    return res