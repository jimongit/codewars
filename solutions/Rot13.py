import string as strg
def rot13(s):
    l =strg.ascii_lowercase
    u=strg.ascii_uppercase
    res=''
    for i in s:
        if(i.islower()): res+=l[(l.index(i)+13)%26]
        elif(i.isupper()):res+=u[(u.index(i)+13)%26]
        else:res+=i
    return res