def first_non_repeating_letter(s):
    s_=s.lower()
    for i in s:
        if(s_.count(i.lower())==1):
            return i
    return ''