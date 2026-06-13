# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        good = 0
        def dfs(root, currMax):
            nonlocal good
            if not root:
                return

            currMax = max(currMax, root.val)
            if root.val>=currMax:
                good+=1

            dfs(root.left, currMax)
            dfs(root.right, currMax)

        dfs(root, float("-inf"))
        return good