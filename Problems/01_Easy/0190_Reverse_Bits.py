class Solution:
    # Pythonic way, easy to understand
    def reverseBits(self, n: int) -> int:
        bit_str = '{0:032b}'.format(n)
        reverse_str = bit_str[::-1]
        return int(reverse_str, 2)
    
    # General way, easy to understand
    def reverseBits_1(self, n):
        reversed = 0
        for i in range(32):
            reverse = reverse << 1
            reversed |= (n >> i) & 0x1
        return reversed
    
    """
    Divide and Conquer! Someway like merge sort.
    For example, if there are 8 bit binary number abcdefgh,
    the process is as follow:
    abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
    
    """
    def reverseBits_2(self, n):
        # For python, there is no 32bit int, so we need to force it 32 bits.
        n = (n >> 16) | (n << 16) & 0xffffffff
        n = ((n & 0xffffffff) >> 8) | ((n & 0xffffffff) << 8) & 0xffffffff
        n = ((n & 0xffffffff) >> 4) | ((n & 0xffffffff) << 4) & 0xffffffff
        n = ((n & 0xffffffff) >> 2) | ((n & 0xffffffff) << 2) & 0xffffffff
        n = ((n & 0xffffffff) >> 1) | ((n & 0xffffffff) << 1) & 0xffffffff
