class Solution:
    def isPalindrome(self, s: str) -> bool:   
        
        text = "".join([c for c in s if c.isalpha() or c.isdigit()]).lower()
        
        return text == text[::-1]
