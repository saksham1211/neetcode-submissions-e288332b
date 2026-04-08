# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def sameTree(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val==q.val:
                return sameTree(p.left, q.left) and sameTree(p.right, q.right)

            else:
                return False

        def dfs(p, q):
            if not p and not q:
                return True
            if not p or not q:
                return False
            if sameTree(p, q):
                return True

            else:
                return dfs(p.left, q) or dfs(p.right, q)
            
        if dfs(root, subRoot):
            return True
        else:
            return False