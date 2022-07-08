#方法一
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #判断正负
        sign = 1 if x>0 else -1
        rst=0
        x=abs(x)
        
        #从x的各位起，提取数字组成rst，直到x为0
        while x:
            rst=rst*10+x%10
            x=x//10
        
        #防止rst溢出
        return sign*rst if -(2**31)-1 < rst < 2**31 else 0


#方法二（不符合储存要求，但只有三行）
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        #判断正负
        sign = 1 if x>0 else -1
        
        #先将x取绝对值，转化为字符串，再倒序该字符串，最后重新变回数字并乘以正负号
        rst = sign * int(str(abs(x))[::-1])
        
        #防止rst溢出
        return rst if -(2**31)-1 < rst < 2**31 else 0