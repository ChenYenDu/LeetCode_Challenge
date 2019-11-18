class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return bin( int(a,2) + int(b,2) )[2:]
    # int(a, 2) turn binary format to integer
    # bin() turn integer to binary
    # [2:] get elements starts from the third element because python use "0b" to identitify number as binary
    # 0x... 16 base  || 0... 8 base
