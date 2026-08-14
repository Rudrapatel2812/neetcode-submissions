class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for a in s:
            if a in "({[":
                stack.append(a)
            elif a== "]":
                if not stack or stack[-1]!="[":
                    return False
                stack.pop()
            elif a==")":
                if not stack or stack[-1]!="(":
                    return False
                stack.pop()
            elif a=="}":
                if not stack or stack[-1]!="{":
                    return False
                stack.pop()
            
            
        return len(stack) == 0
            


        