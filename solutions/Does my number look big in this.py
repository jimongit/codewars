def narcissistic( val):
    str_val =str(val)
    res = 0
    for i in str_val:
        res += int(i)**len(str_val)
    
    return res == val
        
   