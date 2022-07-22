#该程序需在Python3.6或更新的环境下运行
#可以类比第13题
class Solution:
    def intToRoman(self, num: int) -> str:
        #建立字典
        d = {1000: 'M', 900: 'CM', 
             500: 'D', 400: 'CD', 
             100: 'C', 90: 'XC', 
             50: 'L', 40: 'XL', 
             10: 'X', 9: 'IX', 
             5: 'V', 4: 'IV', 
             1: 'I'} 
        
        #建立输出的空字符串
        rst = ""
        
        #在Python3.6+环境中，字典有序，因此循环中i会先为1000，再为900，而不是从1开始
        for i in d:
            #按从大到小的顺序添加对应个数的罗马字符
            rst += (num//i) * d[i]
            #将数字去除已转化为罗马字符的部分
            num %= i
        
        return rst
