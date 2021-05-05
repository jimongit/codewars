def order(s):
    if(s==""):return ''
    s=s.split()
    res=['']*len(s)
    for wrd in s:
        idx=''
        for c in wrd:
            if(c.isdigit()):idx+=c
        i=int(idx)-1
        res[i]=wrd + ' '
    return ''.join(res).rstrip()