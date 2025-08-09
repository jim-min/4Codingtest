import sys
sys.setrecursionlimit(10**6)

class BST:
    def __init__(self, root):
        self.root = Treenode(root)

    def put(self, n):
        self.curr = self.root
        while True:
            if n <= self.curr.n:
                if self.curr.left == None:
                    self.curr.left = Treenode(n)
                    break
                
                else:
                    self.curr = self.curr.left

            else:
                if self.curr.right == None:
                    self.curr.right = Treenode(n)
                    break
                
                else:
                    self.curr = self.curr.right

    def postorder(self, node = None):
        if node == None:
            node = self.root

        if (node.left != None):
            self.postorder(node.left)

        if (node.right != None):
            self.postorder(node.right)

        print(node.n)

class Treenode:
    def __init__(self, n):
        self.n = n
        self.left = None
        self.right = None

# 알고리즘 시작

n = int(sys.stdin.readline())
new_tree = BST(n)

while True:
    try:
        new_tree.put(int(sys.stdin.readline()))

    except:
        break

new_tree.postorder()
