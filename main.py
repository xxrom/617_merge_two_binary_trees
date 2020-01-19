# Definition for a binary tree node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.__dict__)


class Solution:
    def printAll(self, root):
        if root.val != None:
            print(root.val)
        if root != None and root.left != None:
            self.printAll(root.left)
        if root != None and root.right != None:
            self.printAll(root.right)

    def mergeTrees(self, node0: Node, node1: Node, merged: Node = None) -> Node:
        if (node0 != None and node0.val != None) or (node1 != None and node1.val != None):
            val0 = node0.val if node0 != None and node0.val != None else 0
            val1 = node1.val if node1 != None and node1.val != None else 0

            merged = Node(val0 + val1)

            node0Left = node0.left if node0 != None and node0.left != None else None
            node1Left = node1.left if node1 != None and node1.left != None else None

            node0Right = node0.right if node0 != None and node0.right != None else None
            node1Right = node1.right if node1 != None and node1.right != None else None

            if node0Left != None or node1Left != None:
                merged.left = self.mergeTrees(
                    node0Left, node1Left, merged.left)
            if node0Right != None or node1Right != None:
                merged.right = self.mergeTrees(
                    node0Right, node1Right, merged.right)

        return merged


tree0 = Node(1, Node(3, Node(5)), Node(2))
tree1 = Node(2, Node(1, None, Node(4)), Node(3, None, Node(7)))

my = Solution()
merged = my.mergeTrees(tree0, tree1)
my.printAll(merged)

#     3
#  4      5
# 5  4    5  7
