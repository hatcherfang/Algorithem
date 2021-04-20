class TNode(object):
    def __init__(self, value):
        self.value = value
        self.lchild = None
        self.rchild = None


class BiTree(object):
    def __init__(self, L):
        self.L = L
        self.index = 0

    def createTree(self):
        if not self.L:
            return
        root = None
        value = self.L[self.index]
        self.index += 1
        if value > 0:
            root = TNode(value)
            root.lchild = self.createTree()
            root.rchild = self.createTree()
        return root

    def preOrder(self, root):
        if not root:
            return
        print(root.value)
        self.preOrder(root.lchild)
        self.preOrder(root.rchild)

    def midOrder(self, root):
        if not root:
            return
        self.midOrder(root.lchild)
        print(root.value)
        self.midOrder(root.rchild)

    def postOrder(self, root):
        if not root:
            return
        self.postOrder(root.lchild)
        self.postOrder(root.rchild)
        print(root.value)


if __name__ == '__main__':
    L = [1, 3, 2, 0, 0, 5, 0, 0, 4, 0, 0]
    bt = BiTree(L)
    root = bt.createTree()
    print("preOrder:")
    bt.preOrder(root)
    print("midOrder:")
    bt.midOrder(root)
    print("postOrder:")
    bt.postOrder(root)
