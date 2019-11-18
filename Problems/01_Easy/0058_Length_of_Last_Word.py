class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        res = s.split(" ")
        res = list(filter(None, res))  # get rid of empty element after split like "a "
        if not res:
            return 0  # if there are noe space return 0
        return len(res[-1]) # reutrn length of the last element
        # someone user res[-1:][0] and get faster result -> don't know why....
