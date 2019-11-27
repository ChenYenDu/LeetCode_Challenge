class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            try:
                hash_table.pop(i)
            except:
                hash_table[i] = 1
        return hash_table.popitem()[0]
    
    
"""
Bit Manipulation:
A XOR 0 = A
A XOR A = 0
A XOR B XOR A = (A XOR A) XOR B = 0 XR B = B 

也就是說用 XOR 把所有的數字接起來 重複的數字會因為 XOR 變成 0, 最後剩下只有 single value

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = 0
        for i in nums:
            a ^= i
        return a
    
"""
