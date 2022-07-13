class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        m=len(s)
        n=len(p)
        
        #基本思路为DP表，先建立DP表
        #表中，dp[i][j]代表s[0:i-1]和p[0:j-1]的匹配情况，值为True或False，
        #初始化表格为False，除了dp[0][0]为True，代表两个空字符串可以匹配
        dp=[[False]*(n+1) for _ in range(m+1)]
        dp[0][0] = True
        
        #需要考虑的只有'.'和'*'两个特殊字符，其中'.'只需在单个比较中考虑，主要讨论'*'
        #出现'*'有两种情况，第一种为消除了前面一个字符，第二种为留有前面一个字符一次或多次
        #针对这两种情况，将"字符+*"这两个字符视为一个整体，可进行如下考虑
        #第一种情况：将p中这个整体忽略，继续比较
        #第二种情况：将s中第i-1个字符（即当前进行比较的字符）忽略，继续比较。
        #           如当出现某字符被*重复两次时，忽略s中第i-1个字符后，便会变为该字符被*重复一次，再忽略后，便成为了第一种情况

        #填写dp表的第一行，即当s为空字符串的情况
        for j in range(1,n+1):
            #因为s为空字符串，所以只可能有*将p中所有字符删光，对应第一种情况
            dp[0][j]=(p[j-1]=="*") and (j>=2) and (dp[0][j-2])

        for i in range(1,m+1):
            for j in range(1,n+1):
                #first_match判断当前比较的两个字符是否相等，或p为万能字符
                first_match=(p[j-1] in {s[i-1], '.'})
                if p[j-1]=='*':
                    #second_match判断当前比较的s中字符是否等于p中上一个字符，用于第二种情况
                    second_match=(p[j-2] in {s[i-1], '.'})
                    #dp[i][j]=dp[i][j-2]的效果为将"字符+*"整体忽略
                    #dp[i][j]=second_match and dp[i-1][j]的效果为，若s中字符与p中'*'前的字符相等，则忽略s中第i-1个字符
                    dp[i][j]=dp[i][j-2] or (second_match and dp[i-1][j])
                else:
                    #无'*'情况直接比较即可
                    dp[i][j]=first_match and dp[i-1][j-1]

        return dp[m][n]