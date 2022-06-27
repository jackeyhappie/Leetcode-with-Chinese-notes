class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=""
        for i in range(len(s)):
            res=max(self.tool(s,i,i),self.tool(s,i,i+1),res,key=len)
            #tool(s,i,i)用于寻找形如“aba”的奇数个数回文数，tool(s,i,i+1)用于寻找形如“abba”的偶数个数回文数
        return res
            
    #tool函数：从第i个向两侧核对
    def tool(self,s,i,j):
        while i>=0 and j<len(s) and s[i]==s[j]:#j要小于，而不是小于等于len(s)
            i-=1
            j+=1
        return s[i+1:j]#返回第i+1个至第j-1个