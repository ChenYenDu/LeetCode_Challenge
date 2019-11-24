class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0 or numRows ==None:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        
        result = [[1],[1,1]]
        
        while len(result) < numRows:
            prev_row = result[-1]
            cur_row = [1]
            for i in range(1,len(prev_row)):
                cur_row.append(prev_row[i-1]+prev_row[i])
            cur_row.append(1)
            result.append(cur_row)
        return result
            
