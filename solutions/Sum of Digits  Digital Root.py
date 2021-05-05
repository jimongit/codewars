def digital_root(n):
    if(n <10):
        return n
    else:
        n=sum([int(i) for i in list(str(n))])               
    return digital_root(n)