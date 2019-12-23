class Solution:
    def containsNearbyDuplicate(self, nums, k):
        if nums == None:
            return false
        
        ht = {}
        
        for i in range(len(nums)):
            if nums[i] in ht:
                if (i - ht[nums[i]]) <= k:
                    return True
                else:
                    ht[nums[i]] = i
            else:
                ht[nums[i]] = i
            
        return False
