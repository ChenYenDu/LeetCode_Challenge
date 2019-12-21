class Solution:
    '''
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
    
    '''
    '''
    # Sorting
    # Time Complexity: O(n logn) 
    # Space Complexity: O(1)
    def containsDuplicate(self, nums: List[int]) -> bool:
        if nums == None:
            return False
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                return True
        return False
    '''
    # Hash Table
    # Time Complexity: O(n)
    # Space Complexity O(n)
    def containsDuplicate(self, nums: List[int]) -> bool:
        hashTable = {}
        for i in range(len(nums)):
            if nums[i] in hashTable:
                return True
            hashTable[nums[i]] = 1
        return False
            
