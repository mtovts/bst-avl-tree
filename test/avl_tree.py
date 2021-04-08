import unittest

from tree import AVLNode, AVLTree


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.avl_tree = self._get_avl_tree()
        self.small_avl_tree = self._get_small_avl_tree()

    def test_find_min(self) -> None:
        self.assertEqual(self.avl_tree.find_min().value, 11)

    def test_find_max(self) -> None:
        self.assertEqual(self.avl_tree.find_max().value, 99)

    def test_successor(self) -> None:
        self.assertEqual(self.avl_tree.successor(node=self.avl_tree.root).value, 50)
        self.assertEqual(self.avl_tree.successor(node=self.avl_tree.root.right.right.left).value, 91)
        self.assertEqual(self.avl_tree.successor(node=self.avl_tree.root.left.left).value, 20)
        self.assertEqual(self.avl_tree.successor(node=self.avl_tree.root.left.right.right).value, 41)
        self.assertEqual(self.avl_tree.successor(node=self.avl_tree.root.right.right.right), None)

    def test_predecessor(self) -> None:
        self.assertEqual(self.avl_tree.predecessor(node=self.avl_tree.root).value, 32)
        self.assertEqual(self.avl_tree.predecessor(node=self.avl_tree.root.right.right.left).value, 65)
        self.assertEqual(self.avl_tree.predecessor(node=self.avl_tree.root.left.left), None)
        self.assertEqual(self.avl_tree.predecessor(node=self.avl_tree.root.left.right.right).value, 29)

    def test_search(self):
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=11)).value, 11)
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=20)).value, 20)
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=41)).value, 41)
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=99)).value, 99)
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=50)).value, 50)
        self.assertEqual(self.avl_tree.search(node=AVLNode(value=13)), None)

    def test_inorder_traversal(self) -> None:
        self.assertListEqual(self.avl_tree.inorder_traversal(), [11, 20, 29, 32, 41, 50, 65, 72, 91, 99])

    def test_preorder_traversal(self) -> None:
        self.assertListEqual(self.avl_tree.preorder_traversal(), [41, 20, 11, 29, 32, 65, 50, 91, 72, 99])

    def test_postorder_traversal(self) -> None:
        self.assertListEqual(self.avl_tree.postorder_traversal(), [11, 32, 29, 20, 50, 72, 99, 91, 65, 41])

    def test_left_rotation(self) -> None:
        self.small_avl_tree.rotate_right(node=self.small_avl_tree.root)

        self.assertEqual(self.small_avl_tree.root.value, 2)
        self.assertEqual(self.small_avl_tree.root.left.value, 1)
        self.assertEqual(self.small_avl_tree.root.right.value, 4)
        self.assertEqual(self.small_avl_tree.root.right.left.value, 3)
        self.assertEqual(self.small_avl_tree.root.right.right.value, 5)

    def test_left_rotation(self) -> None:
        self.small_avl_tree.rotate_right(node=self.small_avl_tree.root)
        self.small_avl_tree.rotate_left(node=self.small_avl_tree.root)

        self.assertEqual(self.small_avl_tree.root.value, 4)
        self.assertEqual(self.small_avl_tree.root.left.value, 2)
        self.assertEqual(self.small_avl_tree.root.right.value, 5)
        self.assertEqual(self.small_avl_tree.root.left.left.value, 1)
        self.assertEqual(self.small_avl_tree.root.left.right.value, 3)

    def test_insert(self) -> None:
        self.avl_tree.insert(node=AVLNode(value=1))
        self.assertListEqual(self.avl_tree.inorder_traversal(), [1, 11, 20, 29, 32, 41, 50, 65, 72, 91, 99])
        self.assertEqual(self.avl_tree.is_balanced, True)

        self.avl_tree.insert(node=AVLNode(value=2))
        self.assertListEqual(self.avl_tree.inorder_traversal(), [1, 2, 11, 20, 29, 32, 41, 50, 65, 72, 91, 99])
        self.assertEqual(self.avl_tree.is_balanced, True)

        self.avl_tree.insert(node=AVLNode(value=3))
        self.assertListEqual(self.avl_tree.inorder_traversal(), [1, 2, 3, 11, 20, 29, 32, 41, 50, 65, 72, 91, 99])
        self.assertEqual(self.avl_tree.is_balanced, True)

        self.avl_tree.insert(node=AVLNode(value=101))
        self.assertListEqual(self.avl_tree.inorder_traversal(), [1, 2, 3, 11, 20, 29, 32, 41, 50, 65, 72, 91, 99, 101])
        self.assertEqual(self.avl_tree.is_balanced, True)

    @staticmethod
    def _get_small_avl_tree() -> AVLTree:
        """    4
              / \
             2   5
            / \
           1   3
        """
        avl_tree = AVLTree(root=AVLNode(value=4))
        AVLNode(value=2, parent=avl_tree.root)
        AVLNode(value=5, parent=avl_tree.root)

        AVLNode(value=1, parent=avl_tree.root.left)
        AVLNode(value=3, parent=avl_tree.root.left)
        return avl_tree

    @staticmethod
    def _get_avl_tree() -> AVLTree:
        """    41
              / \
            20   65
           / \   / \
         11  29 50  91
              \     / \
              32  72  99
        """
        avl_tree = AVLTree(root=AVLNode(value=41))
        AVLNode(value=20, parent=avl_tree.root)
        AVLNode(value=65, parent=avl_tree.root)

        AVLNode(value=11, parent=avl_tree.root.left)
        AVLNode(value=29, parent=avl_tree.root.left)
        AVLNode(value=50, parent=avl_tree.root.right)
        AVLNode(value=91, parent=avl_tree.root.right)

        AVLNode(value=32, parent=avl_tree.root.left.right)
        AVLNode(value=72, parent=avl_tree.root.right.right)
        AVLNode(value=99, parent=avl_tree.root.right.right)
        return avl_tree


if __name__ == '__main__':
    unittest.main()
