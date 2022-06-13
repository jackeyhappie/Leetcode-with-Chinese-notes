class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        longest=begin=0
        useddic={}#建立出现过字母的字典，标签为字母，内容为目前最后的出现位置
        for i, a in enumerate(s):
            if (a in useddic) and (begin<=useddic[a]):#begin<=useddic[a]为了防止之前出现过，但当前计数的字符串中未出现而错误中断
                begin=useddic[a]+1
            else:
                longest=max(longest,i-begin+1)#植树问题
            useddic[a]=i#更新位置
        return longest