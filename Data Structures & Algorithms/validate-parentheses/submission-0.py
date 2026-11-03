class Solution:
    def isValid(self, s: str) -> bool:
        
        pairs = {')':'(', '}':'{', ']':'['}
        stack = []

        for c in s:
            if c in pairs: # c is a closer 
                if not stack or stack[-1] != pairs[c]: 
                    # no match invalid 
                    return False
                stack.pop()# match -> remove opener
            else: # c is openers
                stack.append(c)
        return not stack # return if stack is empty 
