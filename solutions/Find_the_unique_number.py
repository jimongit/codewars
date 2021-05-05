def find_uniq(arr):
    # arr len is atleast 3
    if (arr[0]==arr[1]):duplicate_element =arr[0]
    else: duplicate_element=arr[2]
    for i in range(len(arr)):
        if(arr[i]!=duplicate_element): return arr[i]
    
    return