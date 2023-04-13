from collections import defaultdict
import sys


class Node:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


def inorder(node):
    if node.left != -1:
        inorder(tree[node.left])

    visited.append(node.val)

    if node.right != -1:
        inorder(tree[node.right])


def similar_inorder(node):
    global cnt

    if node.left != -1:
        similar_inorder(tree[node.left])
        cnt += 1

    if node.val == visited[-1]:
        print(cnt)
        exit(0)
    cnt += 1

    if node.right != -1:
        similar_inorder(tree[node.right])
        cnt += 1


sys.setrecursionlimit(10 ** 6)
N = int(input())
tree = defaultdict(Node)

for _ in range(N):
    a, b, c = map(int, input().split(" "))
    tree[a] = Node(a, b, c)

visited = []
cnt = 0
inorder(tree[1])
similar_inorder(tree[1])
