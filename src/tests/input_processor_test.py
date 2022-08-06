import shutil
import tempfile
from os import path
import unittest

from input_processor import InputProcessor


class TestInputProcessor(unittest.TestCase):

    def setUp(self):
        self.ip = InputProcessor()
        self.test_file = "src/tests/test_file.txt"

    def test_clear_content(self):
        self.ip.input = "test input"
        self.ip.tokenized_input = ["test", "input"]
        self.ip.clear_content()
        self.assertEqual(self.ip.input, None)
        self.assertEqual((self.ip.tokenized_input), [])

    def test_read_file(self):
        result = self.ip._read_file(self.test_file)
        self.assertTrue(result)
        self.assertEqual(self.ip.input, "Test input.\nWith two lines")

    def test_read_file_throws_exception_if_file_does_not_exist(self):
        result = self.ip._read_file("non_existent.txt")
        self.assertFalse(result)
        self.assertIsNone(self.ip.input)

    def test_tokenize_input(self):
        self.ip.input = "First sentence to tokenize. Second with a comma, and a dot."
        self.ip._tokenize_input()
        expected_result = [["first", "sentence", "to", "tokenize"], [
            "second", "with", "a", "comma", ",", "and", "a", "dot"]]
        self.assertEqual(self.ip.tokenized_input, expected_result)

    def test_remove_punctuation(self):
        sentence = "to be removed:.!? to keep:',-"
        result = self.ip._remove_punctuation(sentence)
        self.assertEqual(result, "to be removed to keep',-")

    def test_read_and_preprocess_input(self):
        result = self.ip.read_and_preprocess_input(self.test_file)
        self.assertEqual(result, [["test", "input"], ["with", "two", "lines"]])
