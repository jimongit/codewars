def find_even_index(arr):        
    for i in range(len(arr)):
        r=0 if i==len(arr)-1 else sum(arr[(i+1):])
        l=0 if i==0 else sum(arr[:i])
        if(l==r):
            return i
        elif(i==0 and r==0):return 0
    return -1