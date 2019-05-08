# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        res = []
        if root == None:
            return res
        if root.left == None and root.right == None:
            res.append(str(root.val))
            return res
        leftS = self.binaryTreePaths(root.left)
        for i in range(len(leftS)):
            res.append(str(root.val) + '->' + leftS[i])
        rightS = self.binaryTreePaths(root.right)
        for i in range(len(rightS)):
            res.append(str(root.val) + '->' + rightS[i])
        return res
