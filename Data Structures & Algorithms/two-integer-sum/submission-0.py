class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l=[]
        sum=0
        n=len(nums)
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j]==target:
                    l.append(i)
                    l.append(j)
        return l
                    

        