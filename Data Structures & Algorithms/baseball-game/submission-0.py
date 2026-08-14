class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for s in operations:
            if s=="C":
                stack.pop()
            elif s=="D":
                a= stack[-1]
                stack.append(a*2)
            elif s=="+":
                a=stack[-1]
                b=stack[-2]
                stack.append(a+b)
            else:
                stack.append(int(s))

        return sum(stack)
            

                
                