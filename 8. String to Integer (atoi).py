class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s=s.strip(' ')#去除首尾的空格
        sign=1#定义正负号
        ctsgn=True#用于只判断一次字符是否为正负号
        rst=0#输出结果
        
        for i in range(len(s)):       
            #先判断正负，并且只判断一次
            if ctsgn and s[i] in ['+','-']:
                if s[i]=='-':
                    sign=-1
                ctsgn=False
                continue
            
            #判断是否为数字
            if s[i].isdigit():
                ctsgn=False
                rst=rst*10+int(s[i])
            else:
                break
        return max(-2**31, min(sign * rst,2**31-1))#防止溢出