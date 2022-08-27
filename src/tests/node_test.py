import unittest
from collections import Counter

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

    def test_random_node_returns_weighted_results(self):
        node_1 = Node("second")
        node_2 = Node("first")
        node_3 = Node("third")
        node_1.count = 10
        node_2.count = 15
        node_3.count = 5
        choices = [node_1, node_2, node_3]
        result = Counter(Node.get_random_node(choices) for _ in range(1000))
        self.assertLess(result[node_3], result[node_1])
        self.assertLess(result[node_1], result[node_2])

    def test_get_random_node_returns_weighted_results(self):
        node_1 = Node("second")
        node_2 = Node("first")
        node_3 = Node("third")
        node_1.count = 10
        node_2.count = 15
        node_3.count = 5
        choices = [node_1, node_2, node_3]
        result = Counter(Node.get_random_node(choices) for _ in range(1000))
        self.assertLess(result[node_3], result[node_1])
        self.assertLess(result[node_1], result[node_2])
