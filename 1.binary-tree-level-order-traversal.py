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
        层次遍历
        :param root: 根节点
        :return: list_node -> List
        """

        queue_node = [root]  # 队列
        list_node = []  # 中序遍历存放结果列表

        while queue_node:  # 队列不为空,一直循环

            node = queue_node.pop()  # 出队
            if not node: # 节点为空, 从头开始, 不把空节点放入结果列表
                continue
            list_node.append(node.val) # 把节点数值存放到结果列表
            queue_node.insert(0, node.left) # 左节点先入队
            queue_node.insert(0, node.right) # 右节点后入队

        print(list_node)
        return list_node