class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temps=temperatures
        n=len(temps)
        ans=[0]*n
        stack=[]

        for i, t in enumerate(temps):
            while stack and stack[-1][0]<t:
                stackt, stacki=stack.pop()
                ans[stacki]=i-stacki
            stack.append((t,i))
        return ans

        