class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        #建立数字与字母对应字典
        dic={'1': '', '2': 'abc', '3': 'def',
            '4': 'ghi', '5': 'jkl', '6': 'mno',
            '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
            '0': ' '}
        
        #若digits为空，返回结果为空列表；若digits不为空，设返回结果为列表中一个空字符
        rst=[''] if digits else []

        #顺序处理digits中每个字母
        for num in digits:
            tmp=list()
            #循环该数字对应的每个字母
            for letter in dic[num]:
                #将字母分别添加至原列表中每个字符串的后面
                for word in rst:
                    tmp.append(word+letter)
            rst=tmp
        return rst