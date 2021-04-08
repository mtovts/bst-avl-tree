from typing import Any, Optional

from .bst import BinarySearchTree
from .node import AVLNode


class AVLTree(BinarySearchTree):
    """The Adelson-Velskii & Landis Tree.
    Balanced Binary Search Tree.

    Height of a balanced tree h = O(log N).

    Most AVL Tree operations run in O(log N) time — efficient.

    A vertex v is said to be height-balanced if |v.left.height - v.right.height| ≤ 1.
    """

    def __init__(self, root: AVLNode):
        assert isinstance(root, AVLNode)
        super().__init__(root=root)

    @property
    def height(self) -> int:
        """The lower bound height h > log2 N."""
        if not self._root:
            return -1
        return self._root.height

    @property
    def is_balanced(self) -> bool:
        """A BST is called height-balanced according to the invariant above if
        every node in the BST is height-balanced. Such BST is called AVL Tree.

        That will never change.
        """
        return self._root.is_balanced

    def rotate_right(self, node: AVLNode) -> None:
        """O(1)."""
        assert isinstance(node, AVLNode)
        assert node.left

        w = node.left
        if node is self.root:
            self._root = w

        w.parent = node.parent
        node.parent = w
        node.left = w.right
        if w.right:
            w.right.parent = node
        w.right = node

        w.update_height()
        node.update_height()

    def rotate_left(self, node: AVLNode) -> None:
        """O(1)."""
        assert isinstance(node, AVLNode)
        assert node.right

        w = node.right
        if node is self.root:
            self._root = w

        w.parent = node.parent
        node.parent = w
        node.right = w.left
        if w.left:
            w.left.parent = node
        w.left = node

        w.update_height()
        node.update_height()

    def insert(self, node: AVLNode, start: Optional[AVLNode] = None) -> None:
        """May change the height of the AVL Tree."""
        assert isinstance(node, AVLNode)
        assert start is None or isinstance(start, AVLNode)
        super().insert(node=node, start=start)

        while node.parent:
            if node.balance_factor == 2 and node.left.balance_factor == 1:
                self.rotate_right(node=node)
            elif node.balance_factor == 2 and node.left.balance_factor == -1:
                self.rotate_left(node=node.left)
                self.rotate_right(node=node)
            elif node.balance_factor == -2 and node.right.balance_factor == -1:
                self.rotate_left(node=node)
            elif node.balance_factor == -2 and node.right.balance_factor == 1:
                self.rotate_right(node=node.right)
                self.rotate_left(node=node)
            node = node.parent
            self._root.update_height()

    def remove(self, value: Any) -> None:
        """May change the height h of the AVL Tree."""
        raise NotImplemented
        # update height

    # @classmethod
    # def create(
    #         cls, *, empty: bool = False, random: bool = False, balanced: bool = True
    # ) -> 'AVLTree':
    #     assert balanced is True
    #     return super(AVLTree, cls).create()
