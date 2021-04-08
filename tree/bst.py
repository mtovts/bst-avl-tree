from typing import Callable, Any, Optional

from .node import BSTNode


class BinarySearchTree:
    """A Binary Search Tree (BST) is a binary tree in which each node has only up to
    2 children that satisfies BST property: All nodes in the left subtree of a node must
    hold a value smaller than its own and all nodes in the right subtree of a node must
    hold a value larger than its own.

    Tree has height log2 N < h < N.
    """

    def __init__(self, root: BSTNode):
        assert isinstance(root, BSTNode)

        self._root = root

    def __repr__(self) -> str:
        return f'BST({self.inorder_traversal()})'

    @property
    def root(self) -> BSTNode:
        return self._root

    @property
    def query_operations(self) -> tuple[Callable, ...]:
        return (self.search,
                self.successor,
                self.predecessor,
                self.inorder_traversal,
                self.preorder_traversal,
                self.postorder_traversal,
                self.rank,
                self.select,)

    @property
    def update_operations(self) -> tuple[Callable, ...]:
        return (self.insert,
                self.remove,
                self.create,)

    def find_max(self, start: BSTNode = None) -> BSTNode:
        """Runs in O(h) where h is the height of the tree."""
        current = self._root if start is None else start
        while current.right:
            current = current.right
        return current

    def find_min(self, start: BSTNode = None) -> BSTNode:
        """Runs in O(h) where h is the height of the tree."""
        current = self._root if start is None else start
        while current.left:
            current = current.left
        return current

    # ========== Query operations ==========

    def successor(self, node: BSTNode) -> Optional[BSTNode]:
        """Run in O(h) where h is the height of the tree."""
        assert isinstance(node, BSTNode)

        if node.right:
            return self.find_min(start=node.right)
        else:
            p = node.parent
            t = node
            while p and t == p.right:
                t = p
                p = t.parent
            return p if p else None

    def predecessor(self, node: BSTNode) -> Optional[BSTNode]:
        """Run in O(h) where h is the height of the tree."""
        assert isinstance(node, BSTNode)

        if node.left:
            return self.find_max(start=node.left)
        else:
            p = node.parent
            t = node
            while p and t == p.left:
                t = p
                p = t.parent
            return p if p else None

    def search(self, node: BSTNode, start: BSTNode = None) -> Optional[BSTNode]:
        """Run in O(h) where h is the height of the tree."""
        assert isinstance(node, BSTNode)
        assert start is None or isinstance(start, BSTNode)
        current = self._root if start is None else start

        if current is None:
            return None  # value not found

        elif current.value == node.value:
            return current
        elif current.value < node.value:
            if current.right:
                return self.search(node=node, start=current.right)
            return None
        else:
            if current.left:
                return self.search(node=node, start=current.left)
            return None

    def inorder_traversal(
            self, start: Optional[BSTNode] = None, traversal: list = None
    ) -> list[Any]:
        """Runs in O(N), regardless of the height of the tree."""
        assert start is None or isinstance(start, BSTNode)
        if traversal is None:
            traversal = []
        current = self._root if start is None else start

        if current.left:
            traversal = self.inorder_traversal(start=current.left, traversal=traversal)
        traversal.append(current.value)
        if current.right:
            traversal = self.inorder_traversal(start=current.right, traversal=traversal)
        return traversal

    def preorder_traversal(
            self, start: Optional[BSTNode] = None, traversal: list = None
    ) -> list[Any]:
        """Runs in O(N), regardless of the height of the tree."""
        assert start is None or isinstance(start, BSTNode)
        if traversal is None:
            traversal = []
        current = self._root if start is None else start

        traversal.append(current.value)
        if current.left:
            traversal = self.preorder_traversal(start=current.left, traversal=traversal)
        if current.right:
            traversal = self.preorder_traversal(start=current.right, traversal=traversal)
        return traversal

    def postorder_traversal(
            self, start: Optional[BSTNode] = None, traversal: list = None
    ) -> list[Any]:
        """Runs in O(N), regardless of the height of the tree."""
        assert start is None or isinstance(start, BSTNode)
        if traversal is None:
            traversal = []
        current = self._root if start is None else start

        if current.left:
            traversal = self.postorder_traversal(start=current.left, traversal=traversal)
        if current.right:
            traversal = self.postorder_traversal(start=current.right, traversal=traversal)
        traversal.append(current.value)
        return traversal

    def rank(self, node: BSTNode) -> Optional[int]:
        # assert isinstance(node, BSTNode)
        raise NotImplemented

    def select(self, rank: int) -> Optional[BSTNode]:
        raise NotImplemented

    # ========== Update operations ==========

    def insert(self, node: BSTNode, start: Optional[BSTNode] = None) -> None:
        """Runs in O(h) where h is the height of the tree.
        """
        assert isinstance(node, BSTNode)
        assert start is None or isinstance(start, BSTNode)
        current = self._root if start is None else start

        if current.value > node.value:
            if current.left:
                self.insert(node=node, start=current.left)
            else:
                current.add_child(node=node, to_left=True)
        elif current.value < node.value:
            if current.right:
                self.insert(node=node, start=current.right)
            else:
                current.add_child(node=node, to_right=True)
        else:
            raise ValueError(f'{current} already in tree')

    def remove(self, node: BSTNode) -> None:
        assert isinstance(node, BSTNode)
        node = self.search(node=node)
        if not node:
            raise ValueError(f'{node} not found')

        if node.is_leaf:
            # This part is clearly O(1) — on top of the earlier O(h) search-like effort.
            node.remove()
        elif node.has_one_child:
            # This part is clearly O(1) — on top of the earlier O(h) search-like effort.
            node.parent.add_child(node=node.left or node.right)
            # node.parent = node.left or node.right
            # node._left, node._right = None, None
            # node.remove()
        else:
            # This part requires O(h) due to the need to find the successor node —
            # on top of the earlier O(h) search-like effort.
            # fixme
            node.replace(node=self.successor(node=node))

    @classmethod
    def create(
            cls, *, empty: bool = False, random: bool = False, balanced: bool = False
    ) -> 'BinarySearchTree':
        raise NotImplemented
