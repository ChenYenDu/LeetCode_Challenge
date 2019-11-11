class Solution:
    def romanToInt(self, s: str) -> int:
        transMap = {  # create a translation map
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        result = transMap[s[0]]  # initiate result as the first roman of s
        # s = MVMXCIV, zip(s[1:], s[0:-1])= zip("CMXCIV","MCMXCI") = [(C,M),(M,C),(X,M),(C,X),(I,C),(V,I)]
        for c, p in zip(s[1:], s[0:-1]):
            # same as compare each element in s with the element in front of itself
            result += transMap[c]
            # if the element is smaller than the former one, result should minus twice times of itself
            if transMap[c] > transMap[p]:
                result -= 2 * transMap[p]
        return result
