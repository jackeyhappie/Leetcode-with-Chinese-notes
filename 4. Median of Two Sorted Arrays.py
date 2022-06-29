#方法一
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #使nums2长度短
        N1=len(nums1)
        N2=len(nums2)
        if N1<N2:
            return self.findMedianSortedArrays(self,nums2,nums1)
        
        #分别切割nums1和nums2，使得两者分割左侧的数字数等同与右侧（至多因为奇数个数字而差1）
        #目标得到的正确分割为，num1和num2中左侧的数字即为全部数字中小的一半，右侧的数字即为全部数字中大的一半
        #lo为nums2正确切分处的最小值，hi为最大值，当两者相等时即求得目标值
        lo=0
        hi=N2*2

        while lo<=hi:
            #mid1，mid2分别为nums1和nums2切分处的两倍，两者和根据中位数的定义为总数的一半的两倍，即N1+N2
            mid2=(lo+hi)/2
            mid1=N1+N2-mid2
            #L1，L2为nums1，nums2分割线相邻左侧的数字值，R1，R2同理
            if mid1==0:
                L1=-10**6
            else:
                L1=nums1[(mid1-1)/2]
            if mid2==0:
                L2=-10**6
            else:
                L2=nums2[(mid2-1)/2]
            if mid1==N1*2:
                R1=10**6
            else:
                R1=nums1[mid1/2]
            if mid2==N2*2:
                R2=10**6
            else:
                R2=nums2[mid2/2]
            
            #如果nums1划分左侧的数字大于nums2划分右侧是数字，说明该右侧数字应该在所有数字的左半，因此将nums2的划分线右移一格
            if L1>R2:
                lo=mid2+1
            #如果nums1划分右侧的数字小于nums2划分左侧是数字，说明该左侧数字应该在所有数字的右半，因此将nums2的划分线左移一格
            elif L2>R1:
                hi=mid2-1
            #最终比较一下L1，L2和R1，R2，得到答案
            else:
                return (max(L1,L2)+min(R1,R2))/2
        return -1


#方法二：
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        len1=len(nums1)
        len2=len(nums2)

        #对奇数长度，中位数就是中间数
        if (len1 + len2) % 2 != 0:
            return self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
        else:
        #对偶数长度，中位数就是中间两个数的平均值
            middle1 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2)
            middle2 = self.get_kth(nums1, nums2, 0, len1-1, 0, len2-1, (len1+len2)//2-1)
            return (middle1 + middle2) / 2
    
    #k为目标找到所有数中排在第k个的数
    #start1为nums1中可能包含第k个的数的起始位置，end1为nums1中可能包含第k个的数的最后位置
    def get_kth(self, nums1, nums2, start1, end1, start2, end2, k):
        #若start1 > end1，代表第k个的数在nums2中，同时前k-1个有start1个在nums1中
        if start1 > end1:
            return nums2[k-start1]
        if start2 > end2:
            return nums1[k-start2]
        
        #求取中间值
        middle1 = (start1 + end1) // 2
        middle2 = (start2 + end2) // 2
        middle1_value = nums1[middle1]
        middle2_value = nums2[middle2]
        
        # 若中间值的和小于k，代表第k个的数至少大于middle1_value和middle2_value中的一个（不一定都大于）
        if (middle1 + middle2) < k:
            #若middle1_value > middle2_value，代表k不在nums2的前半中，则将start2更新为middle2+1
            #因为数字的标号没变，所有仍输入k而非k-middle2
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, end1, middle2+1, end2, k)
            else:
                return self.get_kth(nums1, nums2, middle1+1, end1, start2, end2, k)
        # 若中间值的和小于k，代表第k个的数至少小于middle1_value和middle2_value中的一个（不一定都小于）
        else:
            #若middle1_value > middle2_value，代表k不在nums1后半中，则将end1更新为middle1-1
            if middle1_value > middle2_value:
                return self.get_kth(nums1, nums2, start1, middle1-1, start2, end2, k)
            else:
                return self.get_kth(nums1, nums2, start1, end1, start2, middle2-1, k)