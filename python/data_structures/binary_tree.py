"""This module implements binary search tree with classes TreeNode and BinaryTree."""


class TreeNode:
    """Implements node of a BinaryTree with it's value and left and right links to another nodes"""
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinaryTree:
    """Implements Binary search tree, putting bigger values to the right and smaller to the left."""
    def __init__(self):
        self.root = None

    def add(self, current, value):
        """Method to add value to the tree"""
        if self.root is None:
            self.root = TreeNode(value)
        else:
            if value < current.value:
                if current.left is None:
                    current.left = TreeNode(value)
                else:
                    self.add(current.left, value)
            else:
                if current.right is None:
                    current.right = TreeNode(value)
                else:
                    self.add(current.right, value)

    def __repr__(self):
        root = f"     {self.root.value}   \n" \
               f"    /  \\  \n" \
               f" {self.root.left.value}      {self.root.right.value} \n"
        return root

    @staticmethod
    def visit(node):
        """Method to visit the node and print it"""
        if node is not None:
            print(node.value)
        else:
            print(None)

    def preorder_lookup(self, current, node):
        """Looks up the node using preorder to search it."""
        if current == node:
            return node
        if current is not None:
            self.visit(current)
            self.preorder_lookup(current.left, node)
            self.preorder_lookup(current.right, node)

    def delete(self, current, node):
        """Delets the node and it's links"""
        if current != node:
            self.visit(current)
            self.delete(current.left, node)
            self.delete(current.right, node)
        current.value = None


if __name__ == "__main__":
    my_tree = BinaryTree()
    my_tree.add(None, 14)
    my_tree.add(my_tree.root, 10)
    my_tree.add(my_tree.root, 19)
    my_tree.add(my_tree.root, 12)
    print(my_tree.__repr__())
    my_tree.preorder_lookup(my_tree.root, 10)
