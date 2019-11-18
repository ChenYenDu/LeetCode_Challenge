class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0 
        listLen = len(digits)
        
        for i in range(listLen):   # loop through digits to make the tempery answers
            ans += digits[i] * (10 ** (listLen-i-1) )
            
        return [ele for ele in str(ans + 1)]  
	# list comprehension loop through each character of string transfer for answer + 1
