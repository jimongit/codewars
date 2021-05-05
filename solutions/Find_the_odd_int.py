def find_it(arr):
    s_arr = sorted(arr)   
    odd = arr[0]
    count = 0 
    for i in range(len(s_arr)):
        if(i==len(s_arr)-1): return s_arr[len(s_arr)-1]
        if(i>0 and count%2!=0 and s_arr[i]!=s_arr[i-1]):            
            return s_arr[i-1]
        count+=1
            
    return None
