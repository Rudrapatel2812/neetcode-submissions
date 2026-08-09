class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count={}
        for n in nums:
            count[n]=count.get(n,0)+1
        
        result=[]
        ans=len(nums)//3
        for num, freq in count.items():
            if freq>ans:
                result.append(num)
        return result

