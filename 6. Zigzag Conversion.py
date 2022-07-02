#Z字型只是方便理解与图示，本质上只是走来回，无需用Z的形状角度来思考
#方法一
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        leng=len(s)
        #cynum代表每个来回，即‘V’型中，有几个字符
        cynum=numRows*2-2
        if cynum==0:
            return s
        anw=''
        #cycou代表来回或称为‘V’型的个数+1，+1的原因见后
        #下行中+2的原因是//去除了末尾，需多加1才是原本个数
        cycou=leng//cynum+2
        #每一行字符的序号除以cynum后，余数为正负行序号
        #如第一行为0，所以整除；第二行为1，余数为正负1，即1或cynum-1
        #因此可以按该规律逐行输出，而因为涉及到负的余数，所以需要多循环一次，否则结尾处的字符可能会遗漏
        for i in range(numRows):
            for j in range(cycou):
                #防止超范围，并且当i为0和numRows-1时，为第0和最后一行，一次循环只需要输出一个字符
                if (j*cynum-i)>=0 and (j*cynum-i)<leng and i!=0 and i!=numRows-1:
                    anw=anw+s[j*cynum-i]
                if (j*cynum+i)<leng:
                    anw=anw+s[j*cynum+i]
        return anw

#方法二
#运行速度更快
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s

        L = [''] * numRows
        # 等同于如下代码
        # L = []
        # for i in range(0, numRows):
        #     L.append('')
        #如当numRows为3时，L为['','','']
        #L中的字符代表该序号的行下，按顺序排列的字符，如L[0]中即为第0行的字符

        index, step = 0, 1
        #step代表当前是向下走还是向上走，向下为1，向上为0

        for x in s:
            L[index] += x
            #index为0说明在第0行，所以要向下走，step变为1
            if index == 0:
                step = 1
            #index为numRows-1说明在最后一行，所以要向上走，step变为-1
            elif index == numRows -1:
                step = -1
            index += step

        #最后按顺序输出各行即可
        return ''.join(L)