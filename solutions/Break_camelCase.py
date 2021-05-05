def solution(s):
    s_tmp = ''
    for i in s:
        if(i.isupper()):s_tmp+=" " +i
        else:s_tmp+=i
    
    return s_tmp