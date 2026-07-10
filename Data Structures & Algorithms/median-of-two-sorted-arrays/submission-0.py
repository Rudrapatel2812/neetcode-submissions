class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans=0
        nums3=nums1+nums2
        nums3.sort()
        n=len(nums3)
    
        if n % 2 != 0:
            return float(nums3[n // 2])
        else:
            # If the number of elements is even, return the average of the two middle elements
            mid1 = nums3[(n // 2) - 1]
            mid2 = nums3[n // 2]
            return (mid1 + mid2) / 2

        