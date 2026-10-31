class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
      # using hashmap to keep track 
        freq = {}
  
        # Loop through list 
        for num in nums:
        # if check if num not in hash map 
            if num not in freq:
                freq[num] = 1
            else:
                return True
        return False
        
        