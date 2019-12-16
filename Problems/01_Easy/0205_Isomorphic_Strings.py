class Solution:
    
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    # zip 讓相對位置組成 tuple, set去除重複值, 
    # 如果三者長度相同表示為 isomorphic word

