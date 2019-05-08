from collections import Counter
def findAnagrams(s, p):
    """
    :type s: str
    :type p: str
    :rtype: List[int]
    """
    # length = len(p)
    # res = []
    # i = 0
    # while i < len(s) - length + 1:
    #     # if sorted(s[i:j]) == sorted(p):
    #     #     res.append(i)
    #     freq1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     freq2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    #     for m in range(length):
    #         freq1[ord(s[i+m])- 97] += 1
    #         freq2[ord(p[m]) - 97] += 1
    #     if freq1 == freq2:
    #         res.append(i)
    #         while i+length < len(s) and s[i] == s[i+length]:
    #             i += 1
    #             res.append(i)
    #
    #     i += 1
        # if str2nums(s[i:j]) == str2nums(p):
        #     res.append(i)
    # return res
# def str2nums(s):
#     freq = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#     for i in s:
#         freq[ord(i)-97] += 1
#     return freq


    s_len, p_len = len(s), len(p)
    count = p_len
    pChar = Counter(p)

    result = []
    for i in range(s_len):
        if pChar[s[i]] >= 1:
            count -= 1
        pChar[s[i]] -= 1
        if i >= p_len:
            if pChar[s[i - p_len]] >= 0:
                count += 1
            pChar[s[i - p_len]] += 1
        if count == 0:
            result.append(i - p_len + 1)

    return result


s = "abab"
p = "ab"
print(findAnagrams(s, p))
