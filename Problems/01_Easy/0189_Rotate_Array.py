'''
# Brute Force [Time Limit Exceeded]
# O(n*k)
# O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
            previous = nums[len(nums)-1]
            for j in range(len(nums)):
                temp = nums[j]
                nums[j] = previous
                previous = temp


# take the last k element and put them to the head of array
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        nums[:] = nums[-k:] + nums[:-k]
'''
'''
# Classical 3-step array rotation
# 1. reverse the first n - k elements
# 2. reverse the rest of them
# 3. reverse the entire array
# tc: O(n), sc: O(1)
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if k is None or k <= 0:
            return None
        k, end = k % len(nums), len(nums) - 1
        self.reverse(nums, 0, end - k)
        self.reverse(nums, end - k + 1, end)
        self.reverse(nums, 0, end)
        
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start, end = start + 1, end - 1
        
'''
'''
# Recursive solution
# tc: O(n) sc: O(n)
class Solution:
    def rotate(self, nums, k):
        self.helper(0, len(nums)-1-(k%len(nums)), len(nums) -1, nums) # mid belong to the left part
    
    def helper(self, start, mid, end, nums):
        left, right = mid - start, end - mid -1
        if left < 0 or right < 0:
            return
        if left > right:
            for j in range(mid + 1, end + 1):
                nums[j], nums[start] = nums[start], nums[j]
                start += 1
            self.helper(start, mid, end, nums)
        elif right >= left:
            i = mid
            while i >= start:
                nums[i], nums[end] = nums[end], nums[i]
                i, end = i - 1, end - 1
            if left != right:
                self.helper(start, mid, end, nums)
        
'''        
# put the last k elements in correct position (ahead) and do the remaining n-k.
# Once finish swap, the n and k decrease.
class Solution:
    def rotate(self, nums, k):
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in range(k):
                nums[j+i], nums[len(nums)-k+i] = nums[len(nums) - k + i], nums[j + i] # swap
            n, j = n - k, j + k
            k = k % n
        
        

            
