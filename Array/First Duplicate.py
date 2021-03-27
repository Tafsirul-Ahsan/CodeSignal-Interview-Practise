def firstDuplicate(a):
    currentdupe = -1
    dist = len(a)
    if len(a) == 0: return -1
    if len(a) == 1: return -1
    if len(a) == 2 and a[0] == a[1]: return a[0]
    else:
         
         b = list(a)
         b.sort()

        
         for x in (range(len(b)-1)):
             if b[x] == b[x+1]:
                
                 if a[a.index(b[x])+1:].index(b[x]) < dist:
                     dist = a[a.index(b[x])+1:].index(b[x])
                     currentdupe = b[x]
         return currentdupe
a = [2, 1, 3, 5, 3, 2]
print(firstDuplicate(a))
