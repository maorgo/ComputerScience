"""
    This is a python implementation for the Tree data structure
"""

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.__checkType__(left)
        self.__checkType__(right)
        self.leftSon = left
        self.rightSon = right
        self.data = data

    def add_left_son(self, left):
        self.__checkType__(left)
        tmp_node = TreeNode(left)
        self.leftSon = tmp_node

    def add_right_son(self, right):
        self.__checkType__(right)
        tmp_node = TreeNode(right)
        self.rightSon = tmp_node

    def __checkType__(self, node):
        if node is not None and type(node) != type(self):
            raise TypeError('{1} ({0}) is not a tree node type.'.format(type(node), node))

    def __str__(self):
        # return '(node: {0} | left son: {1}| right son: {2})'.format(self.data, self.leftSon, self.rightSon)
        return 'Generic Tree Node Object'

    def print_in_order(self):
        if self is None:
            return
        if self.leftSon is not None:
            self.leftSon.print_in_order()
        print('{} '.format(self.data))
        if self.rightSon is not None:
            self.rightSon.print_in_order()

    def print_pre_order(self):
        if self is None:
            return

        print('{} '.format(self.data))

        if self.leftSon is not None:
            self.leftSon.print_in_order()

        if self.rightSon is not None:
            self.rightSon.print_in_order()

    def print_post_order(self):
        if self is None:
            return
        if self.leftSon is not None:
            self.leftSon.print_in_order()

        if self.rightSon is not None:
            self.rightSon.print_in_order()

        print('{} '.format(self.data))


class BST(TreeNode):
    def __init__(self, key):
        TreeNode.__init__(self, key)

    def insert(self, key):
        tmp_node = BST(key)

        if tmp_node.data < self.data:
            if self.leftSon is None:
                self.leftSon = tmp_node
            else:
                self.leftSon.insert(key)

        elif key >= self.data:
            if self.rightSon is None:
                self.rightSon = tmp_node
            else:
                self.rightSon.insert(key)

    def __str__(self):
        return 'BST Node'
