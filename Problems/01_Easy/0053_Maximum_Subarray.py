class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0] # variable to save result
        tot = nums[0] # variable to save process while looping nums
        for i in range(1,len(nums)):
            tot = max(tot+nums[i], nums[i])  
            # if current iteration is larger then 0 pass it to tot if not add it to tot 
            if  tot > ans: # one tot is larger than ans, pass it to ans
                ans = tot  # and tot keeps changing while looping
        return ans
        
