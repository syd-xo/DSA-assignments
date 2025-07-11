class Tree:
    def __init__(self, value):
        self.right = None
        self.left = None
        self.value = value

    def insert(self, key_value):
        if key_value < self.value:

            if self.left is None:
                self.left = Tree(key_value)
            else:
                self.left.insert(key_value)
        else:
            if self.right is None:
                self.right = Tree(key_value)

    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()

        print(self.value)

        if self.right:
            self.right.inorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()

        if self.right:
            self.right.postorder_traversal()

if __name__ == "__main__":
    tree_obj = Tree(5)

    tree_obj.insert(4)
    tree_obj.insert(3)

    tree_obj.insert(7)
    tree_obj.insert()

print("/n Preorder Traversal")

