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
    def inOrderBottom(self, root):
        """
        中序遍历 非递归
        :param root:  根节点
        :return: list_node -> List
        """
        stack_node = []  # 栈
        list_node = []  # 中序遍历结果存放列表
        node_p = root # 当前节点
        while stack_node or node_p: # 当前节点不为空 or 栈不为空

            while node_p: # 一直移动到最左端
                stack_node.append(node_p) # 节点压栈
                node_p = node_p.left # 指针左移

            node = stack_node.pop() # 出栈
            list_node.append(node.val) # 获取节点数据
            node_p = node.right # 获取有节点

        print(list_node)

        return list_node

    def inOrderBottom_re(self, root):
        """
        中序遍历 递归
        :param root: 根节点
        :return: list_node -> List
        """

        if not root:
            return None
        self.inOrderBottom_re(root.left)
        print(root.val)
        self.inOrderBottom_re(root.right)


