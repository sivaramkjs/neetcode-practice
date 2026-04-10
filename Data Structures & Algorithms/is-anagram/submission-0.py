class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_map = {}
        for s_ch in s:
                s_map[s_ch] = s_map.get(s_ch, 0) + 1
        
        for t_ch in t:
            if t_ch in s_map:
                s_map[t_ch] -= 1
            else:
                return False
        
        for val in s_map.values():
            if val != 0:
                return False
        
        return True