import string

import nltk
from nltk.tag import pos_tag
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')


class InputProcessor:
    def __init__(self):
        self.input = None
        self.tokenized_input = []

    def clear_content(self):
        """ Clears the existing content.
        """
        self.input = None
        self.tokenized_input = []

    def _read_file(self, input_file):
        """ Reads and processes the given file

        Args:
            input_file : input file name as String

        Returns:
            True if file is read succesfully, otherwise False
            
        """
        self.clear_content()
        print(f"Reading file '{input_file}'.")

        try:
            with open(input_file, "r", encoding="utf-8") as file:
                content = file.read()
                self.input = content
            file.close()
        except IOError:
            print(f"Failed to read file '{input_file}'.")
            return False
        return True

    def _tokenize_input(self):
        """ Preprocesses the input to a tokenized form
        Saves a list of sentences, each presented as a list of the tokens it contains to
        self.tokenized_input
        """
        normalized_input = self.input.lower()
        sentences = sent_tokenize(normalized_input)
        for sentence in sentences:
            sentence = self._remove_punctuation(sentence)
            tokenized_sentence = word_tokenize((sentence))
            self.tokenized_input.append((tokenized_sentence))

    def _remove_punctuation(self, sentence):
        """Removes the punctuation from the given sentece. Ignores the agreed excpetions: ' , and -

        Args:
            sentence: String

        Returns:
            The input String without punctuation

        """
        punctuation = string.punctuation.translate(
            {ord(i): None for i in "',-"})
        sentence = sentence.translate({ord(i): None for i in punctuation})
        return sentence

    def read_and_preprocess_input(self, input_file):
        """ Reads the given input file and preprocesses the input to a tokenized form.

        Args:
            input_file: file name as String

        Returns:
            The tokenized input which is a list of sentences, 
            each presented as a list of the string tokens it contains

        """
        self._read_file(input_file)
        self._tokenize_input()
        return self.tokenized_input
