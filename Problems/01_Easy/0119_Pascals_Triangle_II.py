class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

                result = [1] + [0] * rowIndex

        for i in range(rowIndex):
            result[0] = 1
            for j in range(i+1, 0, -1):
                result[j] = result[j]+ result[j-1]
            
        return result
    
        """
        result of current is the result shift and add together
        
        ex. 
        rowIndex = 3
        1,0,0,0 (rownums = 0)
          1,0,0 
        --------  
        1,1,0,0 (rownums = 1)
        0,1,1,0
        --------
        1,2,1,0 (rownums = 2)
        0,1,2,1
        --------
        1,3,3,1 (rownums = 3)
        """

Class Solution2:
'''
Same thought as above but in a efficent way
'''
def getRow(self, rowIndex: int) -> List[int]:
  row = [1]

  for _ in range(1:rownums):
    row = [x+y for x, y in zip([0]+row, row+[0])
  
  return row
