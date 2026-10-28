class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # Put every number in a set.
        #   - lookups like "is 5 in here?" become O(1) instead of O(n)
        #   - duplicates disappear automatically ([1, 2, 2, 3] → {1, 2, 3})
        num_set = set(nums)

        best = 0                                  # longest run found so far
                                                # (stays 0 if nums is empty)

        for num in num_set:                       # look at each distinct number once

            # Is num the START of a run?
            # If num - 1 exists, num is in the middle of some run,
            # and that run will be counted from its real start. Skip it,
            # so no run is ever counted more than once.
            if num - 1 not in num_set:

                length = 1                        # the run so far is just num itself

                # Walk up the run one value at a time:
                #   num + 1, num + 2, num + 3, ... while each one exists.
                # num + length is always "the next value after the run so far".
                while num + length in num_set:
                    length += 1                   # found it: the run is one longer

                best = max(best, length)          # keep the longest run seen

        return best