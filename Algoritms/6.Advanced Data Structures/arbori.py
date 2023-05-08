class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def pre_order_traversal(self):
        print(self.value, end=" ")
        if self.left:
            self.left.pre_order_traversal()
        if self.right:
            self.right.pre_order_traversal()

    def in_order_traversal(self):
        if self.left:
            self.left.in_order_traversal()
        print(self.value, end=" ")
        if self.right:
            self.right.in_order_traversal()

    def post_order_traversal(self):
        if self.left:
            self.left.post_order_traversal()
        if self.right:
            self.right.post_order_traversal()
        print(self.value, end=" ")


class BinaryTree:
    def __init__(self):
        self.root = None

    def add_node(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._add_node(value, self.root)

    def _add_node(self, value, node):
        if value < node.value:
            if node.left is not None:
                self._add_node(value, node.left)
            else:
                node.left = Node(value)
        else:
            if node.right is not None:
                self._add_node(value, node.right)
            else:
                node.right = Node(value)


def print_inorder(node):
    if node is not None:
        print_inorder(node.left)
        print(node.value, end=" ")
        print_inorder(node.right)


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(2)
root.left.right = Node(4)
root.right.left = Node(6)
root.right.right = Node(8)

print_inorder(root)


print("Parcurgere in pre-ordine:")
root.pre_order_traversal()

print("Parcurgere in in-ordine:")
root.in_order_traversal()

print(f"Parcurgere in post-ordine:")
root.post_order_traversal()
