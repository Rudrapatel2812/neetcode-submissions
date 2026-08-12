class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans=0
        min_ele=prices[0]

        for i in range(len(prices)):
            min_ele=min(prices[i],min_ele)
            ans=max(ans, (prices[i]-min_ele))
        return ans
        