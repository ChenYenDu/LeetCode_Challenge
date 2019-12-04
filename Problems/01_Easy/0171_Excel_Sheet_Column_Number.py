class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]  # reverse the string
        sum = 0
        for exp, char in enumerate(s):
            # 位置等同於26的幾次方, ord(s) 把字轉成數 65 代表 chr('A')
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum


'''
class Solution:
    def titleToNumber(self, s: str) -> int:
        s = s[::-1]
        res = 0
        for i in s:
            res = res*26 + ord(i) - ord('A') + 1  # res 存26的次方數
        return res
'''
