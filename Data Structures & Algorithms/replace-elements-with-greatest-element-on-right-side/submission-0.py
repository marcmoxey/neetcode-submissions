class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
    
        max_val = -1
        for i in range(len(arr) - 1, -1, -1):
            tmp = arr[i]                  # 1. save the original value
            arr[i] = max_val              # 2. overwrite with the biggest value seen to the right
            max_val = max(max_val, tmp)   # 3. update the biggest value using the original
        return arr
            

        