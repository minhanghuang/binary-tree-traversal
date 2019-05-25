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
    def preOrderBottom(self, root):
        """
        先序遍历
        :param root: 根节点
        :return: list_node -> List
        """

        stack_node = [root]  # 栈
        list_node = []  # 先序遍历结果存放列表

        while stack_node: # 栈不为空
            node = stack_node.pop() # 栈顶节点出栈
            if not node: # 节点为空
                continue
            list_node.append(node.val) # 把不为空的节点数值存到列表
            stack_node.append(node.right) # 右节点先压栈
            stack_node.append(node.left) # 左节点后压栈

        print(list_node)

        return list_node

    def preOrderBottom_re(self, root):
        """
        先序遍历 递归
        :param root: 根节点
        :return: list_node -> List
        """

        if not root:
            return None
        print(root.val)
        self.preOrderBottom_re(root.left)
        self.preOrderBottom_re(root.right)


