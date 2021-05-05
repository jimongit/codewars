#- for more optimized solution,search for kadane's algorithm
def max_sequence(arr):
    if(arr==[]): return 0    
    mx=arr[0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            mx=max(sum(arr[i:j+1]),mx)
    if(mx<0):return 0
    return mx


def max_sequence1(arr):
    if(arr==[]): return 0
    f = []
    for i in arr:
        if(i<0): f.append(False)
        else:f.append(True)
    if(all(f)):return 0
    mx=arr[0]
    for i in range(len(arr)):
        for j in range(len(arr)):
            mx=max(sum(arr[i:j+1]),mx)
    return mx
