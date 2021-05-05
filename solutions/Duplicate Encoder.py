def duplicate_encode(s):
    s=s.lower()
    if(s=='' or s==None): return
    lst=[]
    s_res=''
    for i in s:
        lst.append(s.count(i))
    
    for i in range(len(s)):
        s_res+='(' if lst[i]==1 else ')'
    
    return s_res