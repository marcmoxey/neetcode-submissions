class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        total = 0
        for ops in operations:
            if ops == "+":
                # add record
                total = stack[-2] + stack[-1]
                stack.append(total)
            elif ops == "C":
                # remove the previous score 
                stack.pop()
            elif ops == "D":
                # Double the prev score 
                total = stack[-1] * 2
                stack.append(total)
            else:
                # add the record 
                stack.append(int(ops))
        return sum(stack)


        