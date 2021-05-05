def generate_hashtag(s):
    if(s=='' or s==None): return False
    s=''.join([i.title() for i in s.split()])
    res='#'+s if len('#'+s)<=140 else False
    return res