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

    def mergeTrees(self, node0: Node, node1: Node) -> Node:
        if (node0 != None and node0.val != None) or (node1 != None and node1.val != None):
            if node0 == None:
                node0 = Node(0)

            node0.val += node1.val if node1 != None and node1.val != None else 0

            node1Left = node1.left if node1 != None and node1.left != None else None
            node1Right = node1.right if node1 != None and node1.right != None else None

            if node0.left != None or node1Left != None:
                node0.left = self.mergeTrees(
                    node0.left, node1Left)
            if node0.right != None or node1Right != None:
                node0.right = self.mergeTrees(
                    node0.right, node1Right)

        # merged tree - node0
        return node0


tree0 = Node(1, Node(3, Node(5)), Node(2))
tree1 = Node(2, Node(1, None, Node(4)), Node(3, None, Node(7)))

my = Solution()
merged = my.mergeTrees(tree0, tree1)
my.printAll(merged)

#     3
#  4      5
# 5  4    5  7

# with additional merged tree:
# Runtime: 108 ms, faster than 5.41% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 14.1 MB, less than 22.86% of Python3 online submissions for Merge Two Binary Trees.

# without additional tree:
# Runtime: 104 ms, faster than 9.26% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.7 MB, less than 74.29% of Python3 online submissions for Merge Two Binary Trees.

# Runtime: 96 ms, faster than 17.71% of Python3 online submissions for Merge Two Binary Trees.
# Memory Usage: 13.8 MB, less than 68.57% of Python3 online submissions for Merge Two Binary Trees.
