class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x < 0 or (x % 10 == 0 and x != 0)):
            return False

        revertedNumber = 0
        while x > revertedNumber:
            # add remainder of x divided 10 to revertedNumber*10
            revertedNumber = revertedNumber * 10 + (x % 10)
            x //= 10  # remember python will return float if integer were not fully divied, so we use // here to get full result without turing into float
        return x == revertedNumber or x == revertedNumber//10
        # the second condition will be met if length of x are odd, e.g. 121 -> revertedNumber=12, x = 1

# the way convert to string
# def isPalindrome(self, x: int) -> bool:
#   return str(x) = str(x)[::-1]
