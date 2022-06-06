class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x<0 or (x>0 and x%10==0):
            return False

        """
        排除负数，排除0结尾的正数（不包括0）
        不然如10000这类的数会判断错
        """

        reversex=0
        
        while x>reversex:
            reversex=x%10+reversex*10
            x=x//10

        return True if (x==reversex//10 or x==reversex) else False

        """
        将x的一半倒叙转为reversex
        若x为回文数，并且长度为偶数，则两者相等
        长度为奇数时，中间的数会在reversex里，如24842变为24和248，这时x==reversex//10
        """