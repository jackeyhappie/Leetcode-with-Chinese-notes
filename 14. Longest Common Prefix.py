class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        
        if not strs:
            return ""
        
        """
        防止输入为空列表
        """

        for i, letter_group in enumerate(zip(*strs)):
            if len(set(letter_group)) > 1:
                return strs[0][:i]
        
        """
        使用zip(*)将每个字符串的第一、第二……个字母重新组合为字符串，最终得到的字符串个数等同于长度最短的字符串，较长的字符串超出部分会被舍弃
        采用set排除重复后，若大于1，说明所有字符串的[i]字母（从0开始算）不完全一致
        则任一字符串的前i个字母就是答案
        """

        else:
            return min(strs)
        """
        防止前缀与最短的字符串完全相同
        """