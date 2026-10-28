class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        best = 0 

        for num in num_set:
            if  num - 1 not in num_set: # is this the start of a run
                length = 1
                while num + length  in num_set: # does the run continue
                    length += 1 
                best = max(best, length)
        return best 
        