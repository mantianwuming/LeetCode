def intToString(num):
    s = ''
    if num == 0:
        return '0'
    if num < 0:
        num = -1*num
        while num != 0:
            s += chr(ord('0') + num%10)
            num = int(num/10)
        s += '-'
        s = list(s)
        s.reverse()
        s = ''.join(s)
        return s
    while num != 0:
        s += chr(ord('0') + num%10)
        num = int(num/10)
        s = list(s)
        s.reverse()
        s = ''.join(s)
    return s

num = 111

print(intToString(num))
