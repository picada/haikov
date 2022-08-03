import pytest
import unittest

from node import Node
from trie import Trie


class TestTrie(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def _pass_fixtures(self, capsys):
        self.capsys = capsys

    def setUp(self):
        self.tokens = [
            ["this", "is", "first", "."],
            ["this", "is", "second", "."]
            ]
        self.segment = ["test", "segment"] 
        self.trie = Trie(self.tokens, 2)
        self.root = self.trie.root

    def assertNodeIsCorrect(self, node, value, count, children_count):
        self.assertEqual(node.value, value)
        self.assertEqual(node.count, count)
        self.assertEqual(len(node.children), children_count)

    def test_trie_is_initialized_with_emtpy_root_node(self):
        self.assertIsNotNone(self.root)
        self.assertEqual(self.root.value, "")
        self.assertEqual(self.root.children, {})

    def test_trie_is_initialized_with_correct_data(self):
        self.assertEqual(self.trie.input_text, self.tokens)
        self.assertEqual(self.trie.depth, 2)
    
    def test_create_add_segment(self):
        self.trie._add_segment(self.segment)

        children_keys = [*self.root.children]
        self.assertEqual(children_keys, ["test"])

        child_node = self.root.children["test"]
        self.assertNodeIsCorrect(child_node, "test", 1, 1)

        grandchildren_keys = [*child_node.children]
        self.assertEqual(grandchildren_keys, ["segment"])
    
        grandchild_node = child_node.children["segment"]
        self.assertNodeIsCorrect(grandchild_node, "segment", 1, 0)

    def test_create_add_segment_increases_count(self):
        self.trie._add_segment(self.segment)
        self.trie._add_segment(["test", "more"])

        children_keys = [*self.root.children]
        self.assertEqual(children_keys, ["test"])

        child_node = self.root.children["test"]
        self.assertNodeIsCorrect(child_node, "test", 2, 2)

    def test_find_segment(self):
        self.trie._add_segment(self.segment)
        result = self.trie.find_segment(["test", "segment"])
        self.assertNodeIsCorrect(result, "segment", 1, 0)

    def test_find_segment_returns_none_when_no_match(self):
        self.trie._add_segment(self.segment)
        result = self.trie.find_segment(["not", "the", "segment"])
        self.assertIsNone(result)
    
    def test_create_trie(self):
        self.trie.create_trie()
        children = self.trie.root.children
        expected_root_children_keys = ["this", "is", "first", "second"]
        root_children_keys = [*children]
        self.assertEqual(root_children_keys, expected_root_children_keys)

        first_node = children["this"]
        self.assertEqual(first_node.count, 2)

        for key in expected_root_children_keys:
            self.assertNotEqual(children[key].children, {})

    def test_print_trie(self):
        self.trie.create_trie()
        self.trie.print_trie()
        output = self.capsys.readouterr()
        expected_output = "this:2\n  is:2\nis:2\n  first:1\n  second:1\nfirst:1\n  .:1\nsecond:1\n  .:1\n"
        self.assertEqual(output.out, expected_output)




