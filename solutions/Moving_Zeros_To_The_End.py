def move_zeros(arr):
    arr2=[]
    cnt=0
    for i in range(len(arr)):
        if(type(arr[i])==bool and arr[i]==False or arr[i]!=0):
            arr2.append(arr[i])
        else:cnt+=1

    for i in range(cnt):
        arr2.append(0)
    
    return arr2