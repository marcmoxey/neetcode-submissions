import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        # build the hashmap of number -> count 
        counts = {}
        h = []
       
        for num in nums:
            counts[num] = counts.get(num, 0) + 1


        # Loop over the hashmap and push (count,num) into a heap
        for num, count in counts.items():
            # Keeping it at size k 
            heapq.heappush(h, (count, num))
            if len(h) > k:
                heapq.heappop(h)

        # Return just the nunbers from the heap
        return [num for count, num in h]