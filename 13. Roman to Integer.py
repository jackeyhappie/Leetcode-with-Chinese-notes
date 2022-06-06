"""
顺序遍览一次的死办法
"""
class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        num=0
        s=s+'A'
        for i in range (len(s)):
            if s[i]=='M':
                num+=1000
            if s[i]=='D':
                num+=500
            if s[i]=='C':
                if s[i+1]=="D" or s[i+1]=="M":
                    num-=100
                else:
                    num+=100
            if s[i]=='L':
                num+=50
            if s[i]=='X':
                if s[i+1]=="L" or s[i+1]=="C":
                    num-=10
                else:
                    num+=10
            if s[i]=='V':
                num+=5
            if s[i]=='I':
                if s[i+1]=="V" or s[i+1]=="X":
                    num-=1
                else:
                    num+=1
        return num

"""
以及虽然短一点，但要遍览4次的更傻的办法
class Solution:
    def romanToInt(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number
"""