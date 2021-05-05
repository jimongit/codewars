def iq_test(s):
    s=s.split()
    x=0
    lst=[]
    for i in range(len(s)):
        if(int(s[i])%2==0):lst.append(i+1)
        else: x=i+1
    res = lst[0] if len(lst)==1 else x
    return res