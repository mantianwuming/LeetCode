def fourSumCount(A, B, C, D):
    """
    :type A: List[int]
    :type B: List[int]
    :type C: List[int]
    :type D: List[int]
    :rtype: int
    """
    res = {}
    for i in C:
        for j in D:
            if i + j not in res:
                res[i+j] = 1
            else:
                res[i+j] += 1
    count = 0
    for i in A:
        for j in B:
            num = -(i+j)
            if num in res and res[num] > 0:
                count += res[num]

    return count

A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]
print(fourSumCount(A, B, C, D))
