import unittest

from entities.node import Node


class TestTrie(unittest.TestCase):

    def setUp(self):
        self.node = Node("test")

    def test_node_is_initialized_correctly(self):
        self.assertEqual(self.node.value, "test")
        self.assertEqual(self.node.count, 1)
        self.assertEqual(self.node.children, {})

    def test_create_add_child(self):
        child_node = self.node.add_child("child")
        children = self.node.children
        self.assertDictEqual(children, {"child": child_node})

    def test_find_child(self):
        child_node = self.node.add_child("child")
        result = self.node.find_child("child")
        self.assertEqual(result, child_node)

    def test_find_child_returns_none_if_no_match(self):
        result = self.node.find_child("none")
        self.assertEqual(result, None)
