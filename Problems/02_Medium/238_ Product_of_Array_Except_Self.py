class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums == None:
            return None

        res = [1]

        for i in range(1, len(nums)):
            res.append(res[i-1]*nums[i-1])

        right = 1
        for j in range(len(nums)-1, -1, -1):
            res[j] = res[j]*right
            right = right * nums[j]
        return res

# loop 1: left -> right
# nums: [1, 2, 3, 4]
# res : [1, (1*1), ((1*1)*2), ((1*1)*2)*3]
# res : [1, 1, 2, 6]
# loop 2: right -> left
# initialize a varable right as assign as 1
# nums = [1, 2, 3, 4]
# res =  [1, 1, 3, 6*1], right = 1 * nums[3] = 4
# res =  [1, 1, 3*4, 6], right = 4 * nums[2] = 12
# ...
# finally res = [24, 12, 8, 3]
