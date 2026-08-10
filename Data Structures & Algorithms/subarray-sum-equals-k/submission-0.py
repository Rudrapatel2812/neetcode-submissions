class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count={0:1}
        prefix_sum=0
        count=0

        for num in nums:
            prefix_sum=prefix_sum+num
            needed= prefix_sum-k

            if needed in prefix_count:
                count=count+prefix_count[needed]
            
            if prefix_sum in prefix_count:
                prefix_count[prefix_sum]=prefix_count[prefix_sum]+1
            else:
                prefix_count[prefix_sum]=1
            
        return count


        