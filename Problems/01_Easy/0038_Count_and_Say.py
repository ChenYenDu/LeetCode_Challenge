class Solution:
    def countAndSay(self, n: int) -> str:

        if n == 1:
            return "1"
        else:
            nums = []
            count = 0
            # recursively find the last number until reach n = 2 pre = 1
            prev = self.countAndSay(n-1)
            temp = prev[0]
            for i in range(len(prev)):
                # add one to count if next number is same as the first element of prev (temp)
                if prev[i] == temp:
                    count += 1
                else:
                    # append count and temp to the result if the next number
                    nums.append(str(count))
                    # is current number is not same as temp
                    nums.append(str(temp))
                    temp = prev[i]          # pass current element to temp
                    # count should be initiate to 1 became current element won't be iter again
                    count = 1
            # append count and temp after the loop for the last part
            nums.append(str(count))
            nums.append(str(temp))
            return ''.join(nums)
