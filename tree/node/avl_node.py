from typing import Any, Optional

from .bst_node import BSTNode


class AVLNode(BSTNode):
    """The node of an AVL Tree."""

    __slots__ = ['_height']

    def __init__(self, value: Any, parent: Optional['AVLNode'] = None):
        assert parent is None or isinstance(parent, AVLNode)
        self._height = 0
        super().__init__(value=value, parent=parent)


    @property
    def parent(self) -> Optional['AVLNode']:
        return super().parent

    @parent.setter
    def parent(self, node: Optional['AVLNode']) -> None:
        assert node is None or isinstance(node, AVLNode)
        self._parent = node

    @property
    def right(self) -> Optional['AVLNode']:
        return super().right

    @right.setter
    def right(self, node: Optional['AVLNode']) -> None:
        assert node is None or isinstance(node, AVLNode)
        self._right = node

    @property
    def left(self) -> Optional['AVLNode']:
        return super().left

    @left.setter
    def left(self, node: 'AVLNode') -> None:
        assert isinstance(node, AVLNode)
        self._left = node

    @property
    def height(self) -> int:
        return self._height

    def add_child(
            self, node: 'AVLNode', *, to_left: bool = False, to_right: bool = False
    ) -> None:
        super().add_child(node=node, to_left=to_left, to_right=to_right)
        self.update_height()

    @property
    def left_child_height(self) -> int:
        return 0 if self._left is None else self._left.height

    @property
    def right_child_height(self) -> int:
        return 0 if self._right is None else self._right.height

    def update_height(self) -> None:
        """To have efficient performance, we shall not maintain `height` attribute via
        the O(N) recursive method every time there is an update (Insert(v)/Remove(v))
        operation.

        Instead, we compute O(1) at the back of our insert()/remove() operation.
        """
        self._height = max(self.left_child_height, self.right_child_height) + 1

    @property
    def balance_factor(self) -> int:
        return self.left_child_height - self.right_child_height

    @property
    def is_balanced(self) -> bool:
        return abs(self.balance_factor) <= 1
