# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        ans = [root.val]
        def dfs(root):
            if root==None:
                return 0
            
            lmax=max(0,dfs(root.left))
            rmax=max(0,dfs(root.right))

            ans[0]= max(ans[0],root.val+lmax+rmax)
            return root.val+max(lmax,rmax)
        dfs(root)
        return ans[0]
        
        