class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # ans=0
        # for i in range(len(heights)):
        #     for j in range(i+1, len(heights)):
        #         area=(j-i)*min(heights[i],heights[j])
        #         ans=max(ans, area)
        # return ans

        # ans=0
        # l,r=0,len(heights)-1
        
        # while l<r:
        #     area=(r-l)*min(heights[l],heights[r])
        #     ans=max(area, ans)
        #     if heights[l]<heights[r]:
        #         l+=1
        #     else:
        #         r-=1
        # return ans
        
        n=len(heights)
        i=0
        j=n-1
        ans=0
        while i<j:
            height=min(heights[i],heights[j])
            width=j-i
            area=height*width
            ans=max(area,ans)
            
            if heights[i]<heights[j]:
                i+=1
            else:
                j-=1
                
        return ans







        