class Node():
    def __init__(self, key=0, lchild=None, rchild=None):
        # set key default value as 0
        self.key = key
        self.lchild = lchild
        self.rchild = rchild


class Tree():
    def __init__(self, List):
        # set List as initial value to make sure correct create tree recursivly
        self.List = List
        self.index = 0

    def createTree(self):
        # to create tree by preorder tree, first set the root node
        root = None
        a = self.List[self.index]
        self.index = self.index + 1
        if a > 0:
            root = Node(key=a)
            root.lchild = self.createTree()
            root.rchild = self.createTree()
        return root

    def preOrder(self, root):
        if root is None:
            return
        print "%r " % root.key,
        self.preOrder(root.lchild)
        self.preOrder(root.rchild)

    def midOrder(self, root):
        if root is None:
            return
        self.midOrder(root.lchild)
        print "%r " % root.key,
        self.midOrder(root.rchild)

    def postOrder(self, root):
        if root is None:
            return
        self.postOrder(root.lchild)
        self.postOrder(root.rchild)
        print "%r " % root.key,


class NoRecursiveTree():
    def __init__(self, List):
        # set List as initial value to make sure correct create tree recursivly
        self.List = List
        self.index = 0

    def createTree(self):
        # to create tree by preorder tree, first set the root node
        root = None
        a = self.List[self.index]
        self.index = self.index + 1
        if a > 0:
            root = Node(key=a)
            root.lchild = self.createTree()
            root.rchild = self.createTree()
        return root

    def preOrder(self, root):
        stack = []
        node = root
        while node or stack:
            if node:
                print "%r " % node.key,
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                node = node.rchild

    def midOrder(self, root):
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append(node)
                node = node.lchild
            else:
                node = stack.pop()
                print "%s " % node.key,
                node = node.rchild

    def postOrder(self, root):
        stack = []
        node = root
        while node or stack:
            if node:
                stack.append([node, False])
                node = node.lchild
            else:
                t = stack.pop()
                node = t[0]
                if not t[1]:
                    # first check whether it first access the node, if it is
                    # the node will be put back again and set the flag as True
                    stack.append([node, True])
                    node = node.rchild
                else:
                    print "%r " % node.key,
                    node = None


if __name__ == '__main__':
    # Recursive traverse binary tree
    print "###Recursive function###"
    L = [1, 3, 2, 0, 0, 5, 0, 0, 4, 0, 0]
    t = Tree(L)
    bt = t.createTree()
    print "do preOrder:"
    t.preOrder(bt)
    print
    print "do midOrder:"
    t.midOrder(bt)
    print
    print "do postOrder:"
    t.postOrder(bt)
    print
    # Nonrecursive traverse binary tree
    print "###Nonrecursive function###"
    t2 = NoRecursiveTree(L)
    bt2 = t2.createTree()
    print "do preOrder:"
    t2.preOrder(bt2)
    print
    print "do midOrder:"
    t2.midOrder(bt2)
    print
    print "do postOrder:"
    t2.postOrder(bt2)
    print
