class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_dict = {
            2:['a','b','c'],
            3:['d','e','f'],
            4:['g','h','i'],
            5:['j','k','l'],
            6:['m','n','o'],
            7:['p','q','r','s'],
            8:['t','u','v'],
            9:['w','x','y','z']
        }
        if len(digits) == 0:
            return []
        if len(digits) == 1:
            return num_dict[int(digits[0])]
        result = self.letterCombinations(digits[1:])
        res = []
        for i in result:
            for j in num_dict[int(digits[0])]:
                res.append(j + i)
        return res
        
