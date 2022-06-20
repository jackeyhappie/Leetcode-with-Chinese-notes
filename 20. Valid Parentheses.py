class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #利用堆栈
        temp=[]
        for i in range(len(s)):
            if s[i]=="(":
                temp.append(')')
            elif s[i]=="[":
                temp.append(']')
            elif s[i]=="{":
                temp.append('}')
            else:
                if (temp==[]) or (s[i]!=temp.pop()):#这里两个条件的顺序不能反，否则当temp中只有一个元素时，会先被pop出，变成空列表后再判断它是不是空列表
                    return False    
        if temp==[]:
            return True

#方法二
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        for i in range(len(s)//2+1):
            if len(s)!=0:
                s=s.replace('()','').replace('{}','').replace('[]','')
        return len(s)==0