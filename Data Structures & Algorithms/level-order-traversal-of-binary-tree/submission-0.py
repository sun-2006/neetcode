# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        k=[]
        def level(root,index):
            if not root:
                return None
            if len(k)==index:
                k.append([])
            k[index].append(root.val)
            level(root.left,index+1)
            level(root.right,index+1)
        level(root,0)  
        return k