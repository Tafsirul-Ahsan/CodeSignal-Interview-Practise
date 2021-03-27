def minSubstringWithAllChars(s, t):
    if len(t) == 1:
        return t
    combins = []
    elems_t = list(t)
    len_cand = 1000000
    candidate = ''
    for i in range(len(s)):
        letter = s[i]
        if letter not in elems_t:
            continue
        t1 = list(t)
        t1.remove(letter)
        substring = s[i+1:]
        try:    
            max_index = max([substring.index(j) for j in t1])
        except:
            continue
        new_candidate = s[i:i+max_index+2]
        if len(new_candidate) < len_cand:
            len_cand = len(new_candidate)
            candidate = new_candidate
        

    return candidate
