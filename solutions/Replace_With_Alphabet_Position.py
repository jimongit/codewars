def alphabet_position(s):
    pair=dict([(chr(i),str(i-96)) for i in range(97,97+26)])
    res=[pair.get(i.lower()) for i in s if i.isalpha()]   
    res=' '.join(res)
    return res
    