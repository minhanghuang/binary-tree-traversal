# Definition for a binary tree node.
class TreeNode:
    """
    节点
    """
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        """
        后序遍历 非递归
        :param root: 根节点
        :return: list_node -> List
        """
        stack_node = [root]
        list_node = []

        while stack_node:
            node = stack_node.pop()

            if node.left: # 左孩子不为空
                stack_node.append(node.left) # 左孩子压栈
            if node.right: # 右孩子不为空
                stack_node.append(node.right) # 右孩子压栈

            list_node.append(node.val) # 获取当前指针数值

        list_node.reverse() # 取反
        return list_node


