class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # ans=[]
        # ans1=[]
        # n=len(nums)
        # for i in range(n):
        #     ans.append(nums[i])
        #     ans1.append(nums[i])
        # return ans+ans1

        n=len(nums)
        ans=[0] * (2*n)

        for i in range(n):
            ans[i]=nums[i]
            ans[i+n]=nums[i]
        
        return ans 


        