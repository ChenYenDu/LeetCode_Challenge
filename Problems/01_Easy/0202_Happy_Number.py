class Solution:
    def isHappy(self, n: int) -> bool:
        '''
        Solution:
            create a set to save value been calculated
            if n exist in the set, it's an inifite loop -> return false
            if not and result as 1 -> return true
        '''
        got = set()
        while n != 1 and n not in got:
            got.add(n)
            sum = 0
            while n:
                sum += (n % 10)**2
                n //= 10
                
            n = sum
        
        return n == 1
