
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        best = 0 
        for num in range(len(nums)):
            if nums[num] == 1:
                curr += 1
                best(best,curr)
            else:
                curr = 0
        return best 

        