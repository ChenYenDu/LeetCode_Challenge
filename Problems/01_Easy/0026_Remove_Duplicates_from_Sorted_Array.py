# You should not create new array
# You should return the length of result
# Number of elements you return in nums should be change to the unique element of original list
# Element out of the range you return won't bother


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        cur = 0  # initiate cur to count the position

        for i in range(1, len(nums)):
            if nums[i] != nums[cur]:  # compare front elemnt with later element if same do nothing
                cur += 1
                # if difference alter the one cur points with the one larger do not equal to it
                nums[cur] = nums[i]
        return cur+1   # return the length of the list
