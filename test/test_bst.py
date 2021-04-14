import unittest

from tree import BinarySearchTree, BSTNode


class TestBinarySearchTree(unittest.TestCase):
    def setUp(self) -> None:
        self.balanced_bst = self._get_balanced_bst()

    def test_find_min(self) -> None:
        self.assertEqual(self.balanced_bst.find_min().value, 4)

    def test_find_max(self) -> None:
        self.assertEqual(self.balanced_bst.find_max().value, 71)

    def test_successor(self) -> None:
        self.assertEqual(self.balanced_bst.successor(node=self.balanced_bst.root).value, 23)
        self.assertEqual(self.balanced_bst.successor(node=self.balanced_bst.root.right.right.left).value, 71)
        self.assertEqual(self.balanced_bst.successor(node=self.balanced_bst.root.left.left).value, 5)
        self.assertEqual(self.balanced_bst.successor(node=self.balanced_bst.root.left.right.right).value, 15)
        self.assertEqual(self.balanced_bst.successor(node=self.balanced_bst.root.right.right), None)


    def test_predecessor(self) -> None:
        self.assertEqual(self.balanced_bst.predecessor(node=self.balanced_bst.root).value, 9)
        self.assertEqual(self.balanced_bst.predecessor(node=self.balanced_bst.root.right.right.left).value, 23)
        self.assertEqual(self.balanced_bst.predecessor(node=self.balanced_bst.root.left.left), None)
        self.assertEqual(self.balanced_bst.predecessor(node=self.balanced_bst.root.left.right.right).value, 7)

    def test_search(self):
        self.assertEqual(self.balanced_bst.search(node=BSTNode(value=15)).value, 15)
        self.assertEqual(self.balanced_bst.search(node=BSTNode(value=6)).value, 6)
        self.assertEqual(self.balanced_bst.search(node=BSTNode(value=71)).value, 71)
        self.assertEqual(self.balanced_bst.search(node=BSTNode(value=9)).value, 9)
        self.assertEqual(self.balanced_bst.search(node=BSTNode(value=666)), None)

    def test_inorder_traversal(self) -> None:
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [4, 5, 6, 7, 9, 15, 23, 50, 71])

    def test_preorder_traversal(self) -> None:
        self.assertListEqual(self.balanced_bst.preorder_traversal(), [15, 6, 4, 5, 7, 9, 23, 71, 50])

    def test_postorder_traversal(self) -> None:
        self.assertListEqual(self.balanced_bst.postorder_traversal(), [5, 4, 9, 7, 6, 50, 71, 23, 15])

    def test_insert(self) -> None:
        self.balanced_bst.insert(node=BSTNode(value=37))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [4, 5, 6, 7, 9, 15, 23, 37, 50, 71])

        self.balanced_bst.insert(node=BSTNode(value=3))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [3, 4, 5, 6, 7, 9, 15, 23, 37, 50, 71])

        with self.assertRaises(ValueError):
            self.balanced_bst.insert(node=BSTNode(value=3))

    def test_remove_leaf(self) -> None:
        self.balanced_bst.remove(node=BSTNode(value=5))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [4, 6, 7, 9, 15, 23, 50, 71])

        self.balanced_bst.remove(node=BSTNode(value=50))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [4, 6, 7, 9, 15, 23, 71])

    def test_remove_has_one_child(self) -> None:
        self.balanced_bst.remove(node=BSTNode(value=4))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [5, 6, 7, 9, 15, 23, 50, 71])

        self.balanced_bst.remove(node=BSTNode(value=9))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [5, 6, 7, 15, 23, 50, 71])

        self.balanced_bst.remove(node=BSTNode(value=7))
        self.assertListEqual(self.balanced_bst.inorder_traversal(), [5, 6, 15, 23, 50, 71])

    # def test_remove_has_two_children(self) -> None:
    # # FIXME
    #     self.balanced_bst.remove(node=BSTNode(value=6))
    #     self.assertListEqual(self.balanced_bst.inorder_traversal(), [4, 5, 7, 9, 15, 23, 50, 71])

    @staticmethod
    def _get_balanced_bst() -> BinarySearchTree:
        """    15
              /  \
             6   23
            / \    \
           4  7    71
           \   \   /
           5   9  50
        """
        bst = BinarySearchTree(root=BSTNode(value=15))
        BSTNode(value=6, parent=bst.root)
        BSTNode(value=23, parent=bst.root)

        BSTNode(value=4, parent=bst.root.left)
        BSTNode(value=7, parent=bst.root.left)
        BSTNode(value=71, parent=bst.root.right)

        BSTNode(value=5, parent=bst.root.left.left)
        BSTNode(value=9, parent=bst.root.left.right)
        BSTNode(value=50, parent=bst.root.right.right)
        return bst


if __name__ == '__main__':
    unittest.main()
