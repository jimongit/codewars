def sum_digits(n):
    #-recursive solution
    str_n = str(n)
    sum_n = sum([int(i) for i in str_n])
    if(sum_n<10):return sum_n
    
    return sum_digits(sum_n)