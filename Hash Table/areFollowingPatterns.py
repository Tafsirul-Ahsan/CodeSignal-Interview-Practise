def areFollowingPatterns(strings, patterns):
    Match_strings = []
    Match_patterns = []
    for i in range(len(strings)):
        if strings[i:] == strings[:i]:
            return True
        else:
            return False
    for j in range(len(patterns)):
        if patterns[j:] == patterns[:j]:
            return True
        else:
            return False
            
strings = ["cat", "dog", "dog"] 
patterns = ["a", "b", "b"]

