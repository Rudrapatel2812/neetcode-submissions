# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def dfs(node):
            if not node:
                ans.append("NULL")
                return
            ans.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        ans = []
        dfs(root)
        return " ".join(ans)


    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        self.i = 0
        data = data.split()
        
        def dfs():
            if data[self.i] == "NULL":
                self.i += 1
                return None
            node = TreeNode(int(data[self.i]))
            self.i += 1
            node.left = dfs()
            node.right = dfs()
            return node
        
        return dfs()