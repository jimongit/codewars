def solution(s):
    mx=0
    for i in range(len(s)):
        if((i+5)<=len(s)):
            mx=max(int(s[i:i+5]),mx)
    return mx