class Solution:
    def reverse(self, x: int) -> int:
        intMax = (2 ** 31) - 1  # got to be causious about the range of integer
        intMin = - 2 ** 31
        str_int = str(x)
        if x < 0:
            result = -1 * int(str_int[:0:-1])
            # check if result is less than the lower border of integer
            return 0 if result < intMin else result
        result = int(str_int[::-1])
        # check if result is larger than the topper border of integer
        return 0 if result > intMax else result
