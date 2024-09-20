class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # summ = 0
        res = nums[0]
        dictt = {}
        for i in range(len(nums)):
            summ = 0
            for j in range(i,len(nums)):
                summ = summ + nums[j]
                res = max(summ,res)
        return res                