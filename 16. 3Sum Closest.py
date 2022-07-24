#与15几乎一致
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #rst为返回值，minus为目前最小差
        rst=0
        minus=2*(10**4)
        
        #对nums排序
        nums.sort()

        #循环len(nums)-2次，因为每次需要3个数学来加和
        for i in range(len(nums)-2):
            #为了加快运算速度，跳过相同的数字
            if i>0 and nums[i]==nums[i-1]:
                 continue
                    
            #第二、第三个数字分别取下一个和最后一个
            j=i+1
            k=len(nums)-1

            while j<k:
                s=nums[i]+nums[j]+nums[k]
            
                #判断是不是目前最小差
                if abs(s-target)<minus:
                    rst=s
                    minus=abs(s-target)
                
                #当三者和小于目标，增大第二个数；当三者和大于目标，减小第三个数
                if s>target:
                    k-=1
                elif s<target:
                    j+=1
                #当三者和等于目标，直接返回目标
                else:
                    return target
        
        return rst