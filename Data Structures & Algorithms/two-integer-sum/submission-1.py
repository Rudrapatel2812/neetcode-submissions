class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        seen= {}
        for i in range(n):
            a=target-nums[i]
            if a in seen:
                return [seen[a],i] 
            
            seen[nums[i]]=i

            
        

        