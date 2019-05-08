import functools
a = [[1,2],[2,3],[1,3],[1,4]]
def compare(x,y):
    if x[1] > y[1]:
        return 1
    elif x[1] < y[1]:
        return -1
    elif x[0] < y[0]:
        return -1
    elif x[0] > y[0]:
        return 1
    else:
        return 0

print(sorted(a,key=functools.cmp_to_key(compare)))
