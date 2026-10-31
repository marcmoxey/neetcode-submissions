
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        best = 0                          # remember the longest streak
        for index in range(len(nums)):    #  was len(nums) - 1, skipped last element
            if nums[index] == 1:
                curr += 1
                best = max(best, curr)    # update best as the streak grows
            else:
                curr = 0
        return best   

        