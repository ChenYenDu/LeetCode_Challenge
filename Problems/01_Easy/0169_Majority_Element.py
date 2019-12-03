# Boyer-Moore Voting ALgroithm
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)

        return candidate


'''
# Divide and Conquer
class Solution:
    def majorityElement(self, nums, lo=0, hi=None):
        def majority_element_rec(lo, hi):
            # base case; the only element in an array of size 1 is the majority
            # element.
            if lo == hi:
                return nums[lo]

            # recurse on left and right halves of this slice.
            mid = (hi-lo)//2 + lo
            left = majority_element_rec(lo, mid)
            right = majority_element_rec(mid+1, hi)

            # if the two halves agree on the majority element, return it.
            if left == right:
                return left

            # otherwise, count each element and return the "winner".
            left_count = sum(1 for i in range(lo, hi+1) if nums[i] == left)
            right_count = sum(1 for i in range(lo, hi+1) if nums[i] == right)

            return left if left_count > right_count else right

        return majority_element_rec(0, len(nums)-1)

TC: O(lgn)
SC: O(lgn)
'''

'''
# Randomization
import random

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums) // 2
        while True:
            candidate = random.choice(nums)
            if sum(1 for elem in nums if elem == candidate) > majority_count:
                return candidate
TC: O(infinit)
SC: O(1)
'''

'''
# Sort
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums)//2]

TC: O(logn)
SC: O(1) or O(n)
'''
    
    
'''
# HashMap
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
        
TC: O(n)
SC: O(n)

'''
        

'''
# Brute force 
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority_count = len(nums)/2
        for num in nums:
            count = sum(1 for ele in nums if ele == num)
            if count > majority_count:
                return num

TC: O(n**2)
SC: O(1)
                
                
'''

