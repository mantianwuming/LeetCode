def pow(x, n):
    assert(n >= 0)
    if n == 0:
        return 1.0
    t = pow(x, n//2)
    if (n % 2):
        return x*t*t
    return t*t

print(pow(3,3))
