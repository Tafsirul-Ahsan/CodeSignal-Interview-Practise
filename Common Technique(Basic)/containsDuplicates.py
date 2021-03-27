def containsDuplicates(a):
    if len(a) == len(set(a)):
        return False
    else:
        return True
a = [1,2,3,1]
result = containsDuplicates(a)
if result:
    print('Yes')
else:
    print('No')
