class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # unique_nums=set(nums)
        # if len(unique_nums)==len(nums):
        #     return False
        # return True

        seen=set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

        