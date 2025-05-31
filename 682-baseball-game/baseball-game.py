class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for op in operations: 
            if op == '+':
                first_num = stack[-1]
                second_num = stack[-2]
                new_num = first_num + second_num
                stack.append(new_num)
            elif op == 'D':
                new_num = stack[-1]
                new_num_doubled = new_num * 2 
                stack.append(new_num_doubled)
            
            elif op == 'C':
                stack.pop()
            else: 
                stack.append(int(op))
            
        return sum(stack)
            
                