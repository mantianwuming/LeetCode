def reverse(s):
    slist = list(s)
    n = len(s)
    for i in range(int(n/2)):
        slist[i], slist[n-1-i] = slist[n-1-i], slist[i]
    s = ''.join(slist)
    return s

s = 'abc'
s = reverse(s)
print(s)
