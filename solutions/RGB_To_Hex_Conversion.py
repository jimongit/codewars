from itertools import permutations as p
def rgb(r, g, b):
    if(r<0):r=0 
    elif(r>255):r=255
    if(g<0):g=0
    elif(g>255):g=255
    if(b<0):b=0
    elif(b>255):b=255    
    lst=[]
    perm= p('01234567890123456789ABCDEFABCDEF',2)
    for i in set(perm):
        if(len(i)==1):
            lst.append('0'+i[0])
        else:lst.append(''.join(i))
    lst=sorted(lst)
    
    hex=lst[r]+lst[g]+lst[b]
    return hex