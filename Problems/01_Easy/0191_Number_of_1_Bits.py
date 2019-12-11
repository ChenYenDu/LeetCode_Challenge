class Solution:
	def hammingWeight(self, n: int) -> int:
	        # Pythonic Way
	        return bin(n).count('1')
    '''
	def hammingWeight(self, n: int) -> int:
		# Loop and Flip
		# space complexity: O(1)
		# time complexity: O(1)
		bits = 0
		mask = 1
		for i in range(32):
		    if (n & mask) != 0 :
		        bits += 1
		    mask <<= 1
		return bits
    '''
    
    '''
	def hammingWeight(self, n: int) -> int:
		# Bit Manipulation Trick
		# Space complexity: O(1)
		# Time complexity: O(1)
		sum = 0
		while n != 0:
		sum += 1
		n &= (n - 1)
		return sum
    '''
    
    '''
	def hammingWeight(self, n: int) -> int:
		return "{0:b}".format(n).count('1')
    '''
    
    '''
	def hammingWeight(self, n: int) -> int:
		if n == 0:
            		return 0
        	return self.hammingWeight(n//2) + n % 2
    
    '''
    
