class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def addChild(self, data):
        if data < self.data:
            if self.left:
                self.left.addChild(data)
            else:
                self.left = TreeNode(data)
        elif data > self.data:
            if self.right:
                self.right.addChild(data)
            else:
                self.right = TreeNode(data)

    def inorder(self):
        k = []

        if self.left:
            k += self.left.inorder()

        k.append(self.data)

        if self.right:
            k += self.right.inorder()

        return k

    def findmin(self):
        if self.left:
            return self.left.findmin()
        else:
            return self

    def findmax(self):
        if self.right:
            return self.right.findmax()
        else:
            return self

    def findparent(self, data):
        parent = self
        if data < self.data:
            if data == self.left.data:
                return parent
            else:
                return self.left.findparent(data)
        elif data > self.data:
            if data == self.right.data:
                return parent
            else:
                return self.right.findparent(data)


def buildtree():
    k = [20, 13, 17, 10, 5, 2, 34, 27, 38, 25, 40]
    t = TreeNode(k[0])
    for i in range(1, len(k)):
        t.addChild(k[i])

    return t


if __name__ == "__main__":
    t = buildtree()
    print(t.inorder())
    print(t.findmin().data)
    print(t.findmax().data)
    print(t.findparent(13).data)
