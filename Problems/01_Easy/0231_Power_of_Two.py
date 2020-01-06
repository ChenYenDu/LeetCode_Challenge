class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n < 1 or n == None:
            return False
        
        while n % 2 == 0:
            n /= 2
        
        return True if n == 1 else False
    
    '''
    # boolean operation
    def isPoserOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) ==0
    
    '''
    
