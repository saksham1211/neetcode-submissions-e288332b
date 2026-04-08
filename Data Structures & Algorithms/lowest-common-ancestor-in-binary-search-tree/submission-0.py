# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        que=deque([root])
  

        while que:
            root=que.popleft()

            if root.val<p.val and root.val<q.val:
                if root.right:
                    que.append(root.right)

            elif root.val>p.val and root.val>q.val:
                if root.left:
                    que.append(root.left)

            else:
                return root