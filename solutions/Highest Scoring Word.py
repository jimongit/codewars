def high(s):
    s=s.split()
    x=dict([(chr(i),i-96) for i in range(97,97+26)])
    lst=[]
    for i in s:
        d=[]
        for z in i:
            d.append(x[z])
        lst.append(d)
    print(lst)
    lst=[sum(i) for i in lst]
    mx=max(lst)
    return s[lst.index(mx)]