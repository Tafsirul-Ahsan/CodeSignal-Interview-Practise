def firstNotRepeatingCharacter(s):
    char_order = []
    counts = {}
    for c in s:
        
        if c in counts:
            counts[c] += 1
        else:
            counts[c] = 1
        char_order.append(c)
    for c in char_order:
        if counts[c] == 1:
            return c
    return '_'
    
print(firstNotRepeatingCharacter("abacabad"))
print(firstNotRepeatingCharacter("abacabaabacaba"))


