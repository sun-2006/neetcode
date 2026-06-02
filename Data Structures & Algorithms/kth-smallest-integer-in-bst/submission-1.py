# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l=[]
        def inorder(node):
            if node:
                inorder(node.left)
                l.append(node.val)
                inorder(node.right)
        inorder(root)
        if len(l)==0 or len(l)<k:
            return None
        else:
            return l[k-1]