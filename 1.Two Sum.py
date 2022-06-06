class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        dictionary={}
        for i in range(len(nums)):
            if nums[i] in dictionary:
                return [dictionary[nums[i]],i]            
            else:
                dictionary[target-nums[i]]=i
        
        """
        建立字典，按顺序查找nums。
        先判断当前查找数是否在字典标签中，
        若不在，将该数的潜在对应数（target-nums[i]）作为字典标签，该数的位置作为内容。
        若在，则匹配成功，读取当前i值和字典内容值输出。
        """