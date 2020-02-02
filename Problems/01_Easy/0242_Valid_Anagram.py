'''
# Sorted
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
'''
'''
# dictionary
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dic1, dic2 = {}, {}
        for item in s:
            dic1[item] = dic1.get(item, 0) + 1
        for item in t:    
            dic2[item] = dic2.get(item, 0) + 1
        
        return dic1 == dic2
        
'''
# Hash Table
# Space Complexity: O(1)
# Time Complexity: O(n)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dic1, dic2 = [0]*26, [0]*26
        for item in s:
            dic1[ord(item) - ord('a')] += 1
        for item in t:
            dic2[ord(item) - ord('a')] += 1
        return dic1 == dic2
