from typing import Any, Optional


class BSTNode:
    """The node of a Binary Search Tree."""

    __slots__ = ['_parent', '_right', '_left', '_value']

    def __init__(self, value: Any, parent: Optional['BSTNode'] = None):
        assert parent is None or isinstance(parent, BSTNode)
        self._parent = parent
        self._right: Optional['BSTNode'] = None
        self._left: Optional['BSTNode'] = None
        self._value = value

        if parent:
            parent.add_child(node=self)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._value})'

    @property
    def parent(self) -> Optional['BSTNode']:
        return self._parent

    @parent.setter
    def parent(self, node: Optional['BSTNode']) -> None:
        node is None or isinstance(node, BSTNode)
        self._parent = node

    @property
    def right(self) -> Optional['BSTNode']:
        return self._right

    @right.setter
    def right(self, node: Optional['BSTNode']) -> None:
        assert node is None or isinstance(node, BSTNode)
        assert not self._right
        self._right = node

    @property
    def left(self) -> Optional['BSTNode']:
        return self._left

    @left.setter
    def left(self, node: Optional['BSTNode']) -> None:
        assert node is None or isinstance(node, BSTNode)
        assert not self._left
        self._left = node

    @property
    def value(self) -> Any:
        return self._value

    @property
    def is_leaf(self) -> bool:
        return not bool(self._left or self._right)

    @property
    def has_one_child(self) -> bool:
        return True if ((self._left and not self._right)
                        or (self._right and not self._left)) else False

    @property
    def has_two_children(self) -> bool:
        return bool(self._left and self._right)

    def add_child(
            self, node: 'BSTNode', *, to_left: bool = False, to_right: bool = False
    ) -> None:
        # assert to_left or to_right
        assert self.value != node.value
        assert not (to_left and to_right)

        if to_left or self._value > node._value:
            self._left = node
            node._parent = self
        elif to_right or self._value < node._value:
            self._right = node
            node._parent = self

    def remove(self) -> None:
        assert self.is_leaf

        if self._parent._value < self._value:
            self._parent._right = None
        else:
            self._parent._left = None

    def replace(self, node: 'BSTNode') -> None:
        assert isinstance(node, BSTNode)
        # TODO
        raise NotImplemented
