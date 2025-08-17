import sys

def preorder(u):
    print(u, end='')
    for i in tree[u]:
        if i == '.':
            continue

        preorder(i)

def inorder(u):
    if tree[u][0] != '.':
        inorder(tree[u][0])

    print(u, end='')

    if tree[u][1] != '.':
        inorder(tree[u][1])

def postorder(u):
    for i in tree[u]:
        if i == '.':
            continue

        postorder(i)

    print(u, end='')
    

n = int(sys.stdin.readline())
tree = {}

for _ in range(n):
    a, b, c = sys.stdin.readline().strip().split()

    tree[a] = [b, c]

preorder('A')
print()

inorder('A')
print()

postorder('A')

