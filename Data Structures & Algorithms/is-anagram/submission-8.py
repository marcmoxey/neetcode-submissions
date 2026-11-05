class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        freq = {}
        freq_b = {}
        

        if len(s) < 0 and len(t) < 0:
            return False 

        for char in s:
            if char not in freq:
                freq[char] = 1 
            else:
                freq[char] += 1

        for char in t:
            if char not in freq_b:
                freq_b[char] = 1 
            else:
                freq_b[char] += 1
        
        return  freq == freq_b
        

       