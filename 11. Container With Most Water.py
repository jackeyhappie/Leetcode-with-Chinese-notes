class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #从两边找起，因为外侧的版拥有更长的宽度，内测的版要是想装更多的水，必须要更高
        #因此可以舍弃外侧版中较低的一根向内移动一格，因为它不可能产生更高的水位
        #先从首位i，j开始
        i=0
        j=len(height)-1
        rst=0

        #当ij重合时，代表以从两侧枚举结束
        while i<j:
            #更新最大值
            rst=max(rst,(j-i)*min(height[i],height[j]))
            
            #舍去较低的板向内移动一格
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return rst
