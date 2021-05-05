def find_outlier(arr):
    odd = 0
    even =0
    for i in range(3):
        if(arr[i]%2==0):even=even+1
        elif(arr[i]%2!=0):odd=odd+1
    
    for j in arr:
        if(odd>1 and j%2==0):return j
        elif(even>1 and j%2!=0):return j
    
    return None
    