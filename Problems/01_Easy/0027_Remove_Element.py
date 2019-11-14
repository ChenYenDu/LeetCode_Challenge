class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) ==0:
            return 0
        
        length = len(nums)   # lenght of nums
        i = 0                # initiate the loop from the first element of nums
        while i < length:
            if nums[i] == val:
                nums[i] = nums[length-1]   # if the iterating element is equal to val, replace the last element of the list
                length -= 1                # reduce the lenght of list in case of the last element are equal to val
            else:
                i += 1     # only when the looping element is no longer equal to val wiil it pass to the next itertiation 
        return i   # finally return the length of element you really iterated
        
