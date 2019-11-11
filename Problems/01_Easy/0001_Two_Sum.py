class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        for i, num in enumerate(nums):
            n = target - num
            if n not in h:
                h[num] = i
            else:
                return [h[n], i]


# nums = [2, 7, 11, 15], target = 9
# enumerate(nums) = [(0,2),(1,7),(2,11),(3,15)]
# i = 0, num = 2 -> n = 7 -> n not in h -> h {2:0}
# i = 1, num = 7 -> n = 2 -> n in h -> return [h[2], 1] -> [0,1]
