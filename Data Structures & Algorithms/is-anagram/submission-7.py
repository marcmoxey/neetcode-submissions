class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Hashmap to keep track of letter and count of both strings
        freq = {}
        freq_b =  {}

        # Check if len < 0 return False 
        if len(s) < 0 and  len(t) < 0:
            return False 

        # Loop for first str to check the letter count 
        for char in s:
            # not in hashmap set the count to 1 
            if char not in freq: 
                freq[char] = 1
            else: 
                # add +1 to the count if it in the hashmap
                freq[char] += 1

        
        # Loop for first str to check the letter count 
        for char in t:
            # not in hashmap set the count to 1 
            if char not in freq_b: 
                freq_b[char] = 1
            else: 
                # add +1 to the count if it in the hashmap
                freq_b[char] += 1

        # compare hashmap
        return freq == freq_b
        