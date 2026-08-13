class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        n=len(nums)
        total=0
        ans=float("inf")
        for j in range(n):
            total+=nums[j]
 
            while total>=target:
                ans=min(ans, (j-i+1))
                total-=nums[i]
                i+=1
                

        return 0 if ans==float("inf") else ans
            


        