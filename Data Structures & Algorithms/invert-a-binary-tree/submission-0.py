# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Base case
        if not root:
            return None

        # Swap the left and right nodes
        temp = root.left
        root.left = root.right
        root.right = temp

        # Continue swapping the nodes, but by doing DFS on left subtree first
        # Then do it on right subtree
        self.invertTree(root.left)
        self.invertTree(root.right)

        # Once DFS and all stack frames are popped off then we are in the first function call
        # Then in the first function call we return the root
        return root
        
        