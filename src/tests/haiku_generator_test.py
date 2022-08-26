import shutil
import tempfile
from os import path
import unittest
from collections import Counter

from services.haiku_generator import HaikuGenerator
from entities.node import Node
from entities.trie import Trie


class TestHaikuGenerator(unittest.TestCase):

    def setUp(self):
        self.data = [["woof", "woof", "woof", "woof"],
                     ["woof", "woof", "woof", "woof"]]
        self.expected_haiku = """woof woof woof woof woof
woof woof woof woof woof woof woof
woof woof woof woof woof"""
        self.hg = HaikuGenerator(2)
        self.hg.trie.create_trie(self.data)

    def test_attempt_haiku_generation_enough_times_before_raising_exception(self):
        self.hg.trie = Trie()
        with self.assertRaises(Exception) as context:
            self.hg.attempt_haiku_generation()
        self.assertEqual(
            "Unable to create a valid haiku with the given input and settings", str(context.exception))
        self.assertEqual(self.hg.attempt, 101)

    def test_generate_haiku_generation(self):
        result = self.hg.attempt_haiku_generation()
        expected = self.expected_haiku.capitalize()
        self.assertEqual(result, expected)

    def test_generate_haiku(self):
        result = self.hg.generate_haiku()
        self.assertEqual(result, self.expected_haiku)

    def test_generate_line(self):
        segment = ["woof"]
        result = self.hg.generate_line(segment)
        self.assertEqual(result, "woof woof woof woof woof\n")

    def test_generate_line_throws_exception_if_segment_not_found_in_trie(self):
        segment = ["not", "in", "trie"]
        with self.assertRaises(Exception) as context:
            self.hg.generate_line(segment)
        self.assertEqual("Segment not found in trie", str(context.exception))

    def test_generate_word(self):
        node = Node()
        node.add_child("meow")
        result = self.hg.generate_word(node, 2)
        self.assertEqual(result, "meow")

    def test_generate_word_fails_if_no_valid_choices(self):
        node = Node()
        with self.assertRaises(Exception) as context:
            self.hg.generate_word(node, 5)
        self.assertEqual(
            "Couldn't find valid choices for the next word.", str(context.exception))

    def test_random_node_returns_weighted_results(self):
        node_1 = Node("second")
        node_2 = Node("first")
        node_3 = Node("third")
        node_1.count = 10
        node_2.count = 15
        node_3.count = 5
        choices = [node_1, node_2, node_3]
        result = Counter(self.hg.get_random_node(choices) for _ in range(1000))
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
        result = Counter(self.hg.get_random_node(choices) for _ in range(1000))
        self.assertLess(result[node_3], result[node_1])
        self.assertLess(result[node_1], result[node_2])

    def test_count_syllables_in_token(self):
        # syllable count for "meow" is 2 and it can be found in the cmu dictionary
        token = "meow"
        result = self.hg._count_syllables_in_token(token)
        self.assertEqual(result, 2)

    def test_count_syllables_in_token_returns_0_if_not_found_in_cmu(self):
        # syllable count for "meow" is 2 and it can be found in the cmu dictionary
        token = "definitely-not-in-dictionary"
        result = self.hg._count_syllables_in_token(token)
        self.assertEqual(result, 0)

    def test_is_valid_token_return_true_for_valid_token(self):
        token = "meow"
        result = self.hg._is_valid_token(token, 2)
        self.assertTrue(result)

    def test_is_valid_token_returns_true_if_token_in_accepted_exceptions(self):
        token = "n't"
        result = self.hg._is_valid_token(token, 4)
        self.assertTrue(result)

    def test_is_valid_token_returns_false_when_not_enough_syllables_left(self):
        token = "meow"
        result = self.hg._is_valid_token(token, 1)
        self.assertFalse(result)

    def test_is_valid_token_returns_false_when_token_not_in_dictionary(self):
        token = "asdfadf"
        result = self.hg._is_valid_token(token, 10)
        self.assertFalse(result)

    def test_is_valid_token_returns_false_when_first_token_in_line_is_not_alpha(self):
        token = "'s"
        result = self.hg._is_valid_token(token, 5)
        self.assertFalse(result)

    def test_is_valid_token_returns_false_when_last_token_in_haiku_is_stopword(self):
        token = "and"
        self.hg._line = 3
        result = self.hg._is_valid_token(token, 1)
        self.assertFalse(result)

    def _is_valid_haiku(self):
        result = self.hg._is_valid_haiku(self.expected_haiku)
        self.asserTrue(result)

    def test_is_valid_haiku_returns_false_with_wrong_line_count(self):
        haiku = "woof woof\nwoof woof"
        result = self.hg._is_valid_haiku(haiku)
        self.assertFalse(result)

    def test_is_valid_haiku_returns_false_with_wrong_syllable_count(self):
        haiku = self.expected_haiku[:-4]
        result = self.hg._is_valid_haiku(haiku)
        self.assertFalse(result)

    def test_change_degree(self):
        self.hg.change_degree(4)
        self.assertEqual(self.hg._degree, 4)
        self.assertEqual(self.hg.trie.depth, 5)
