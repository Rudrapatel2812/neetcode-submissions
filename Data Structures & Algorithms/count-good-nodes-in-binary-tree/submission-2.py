# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node,Maxval):
            if not node:
                return 0

            res=1 if node.val>=Maxval else 0
            Maxval=max(Maxval,node.val)
            res+=dfs(node.left,Maxval)
            res+=dfs(node.right,Maxval)
            return res
            
        return dfs(root,root.val)