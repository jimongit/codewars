def anagrams(word, words):
    s_word=sorted(word)
    lst=[]
    for i in words:
        if(sorted(i)==s_word):
            lst.append(i)
    return lst