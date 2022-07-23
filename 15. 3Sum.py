class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        #创建结果空列表
        rst=[]
        #对输入列表从小到大排序
        nums.sort()
        #循环len(nums)-2次，因为每次需要3个数学来加和
        for i in range(len(nums)-2):
            #因为不能出现重复的组和，所以跳过相同的数字
            if i>0 and nums[i]==nums[i-1]:
                 continue
            #第二、第三个数字分别取下一个和最后一个
            l, r=i+1, len(nums)-1
            
            while l<r:
                s=nums[i]+nums[l]+nums[r]
                #当三者和小于零，增大第二个数；当三者和大于零，减小第三个数
                if s<0:
                    l+=1 
                elif s>0:
                    r-=1
                #当三者和等于0时，将该组会加入结果，同时排除重复数字的情况
                else:
                    rst.append((nums[i], nums[l], nums[r]))
                    while l<r and nums[l]==nums[l+1]:
                        l+=1
                    while l<r and nums[r]==nums[r-1]:
                        r-=1
                    #第二，第三个数字同时改变，进行下组的寻找
                    l+=1; r-=1
        return rst