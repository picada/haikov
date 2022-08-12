import random

import nltk
from nltk.corpus import cmudict, stopwords
from nltk.tokenize import word_tokenize

from trie import Trie

nltk.download('cmudict')
nltk.download('stopwords')
syllable_dict = cmudict.dict()

MAX_ATTEMPTS = 100


class HaikuGenerator:
    def __init__(self, degree):
        self.attempt = 1
        self._max_attempts = MAX_ATTEMPTS
        self._line = 1
        self._degree = degree
        self.trie = Trie(degree + 1)
        self.syllable_limits = {1: 5, 2: 7, 3: 5}

    def attempt_haiku_generation(self):
        """Attempst to generate a valid haiku with the current settings. If a valid haiku cannot
        be created with attempt limit defined in MAX_ATTEMPTS, give up.

        Returns:
            The formatted generated haiku as a string
        """
        self.attempt = 1
        while self.attempt <= self._max_attempts:
            haiku = self.generate_haiku()
            if self._is_valid_haiku(haiku):
                return self.get_formatted_haiku(haiku)
            self.attempt += 1
        raise Exception(
            "Unable to create a valid haiku with the given input and settings")

    def generate_haiku(self):
        """Attempst to generate a valid haiku with the current settings. For the time
        being, the first word is picked by random

        Returns:
            The generated haiku as a string
        """
        haiku = ""
        self._line = 1
        tokens = [*self.trie.root.children]
        choices = [token for token in tokens if token.isalpha()]
        if not choices:
            return haiku
        first_word = random.choices(choices)[0]
        segment = [first_word]
        while self._line <= 3:
            try:
                line = self.generate_line(segment)
                haiku += line
            # todo: improve error handling
            except Exception:  # pylint: disable=broad-except
                break
            self._line += 1
        return haiku

    def generate_line(self, segment):
        """Attempst to generate a new line based on the given segment.
        The amount of syllables in the line is dictaded by self.syllable_limits
        and self._line

        Args:
            segment: Array of arrays of strings

        Returns:
            The generated line as a string
        """
        line = segment[0] if self._line == 1 else ""
        syllable_limit = self.syllable_limits[self._line]
        remaining_syllables = syllable_limit - self._count_syllables_in_line(line)

        while remaining_syllables > 0:
            node = self.trie.find_segment(segment)
            if not node:
                raise Exception("Segment not found in trie")
            try:
                token = self.generate_word(node, remaining_syllables)
                if token.isalpha() and remaining_syllables != self.syllable_limits[self._line]:
                    line += " "
                line += token
                segment.append(token)
                if len(segment) > self._degree:
                    segment.pop(0)
                remaining_syllables -= self._count_syllables_in_token(token)
            except Exception as error:
                raise error
        if self._line < 3:
            line += "\n"
        return line

    def generate_word(self, node, remaining_syllables):
        """Attempst to generate a word based on the given node and
        remaining syllables in the line

        Args:
            node: Node object
            remaining_syllables: number of remaining syllables

        Returns:
            The generated word as a string
        """
        choices_all = node.children
        valid_choices = dict(filter(lambda choice: self._is_valid_token(
            choice[0], remaining_syllables), choices_all.items()))
        if not valid_choices:
            raise Exception(
                "Couldn't find valid choices for the next word.")
        values_and_weights = self.get_values_and_weights(
            valid_choices.values())
        token = random.choices(values_and_weights[0], values_and_weights[1])[0]
        return token

    def _count_syllables_in_token(self, value):
        """Counts the number of syllables in a word.
        Each sylllable corresponds to one vowel phoneme in the CMU pronounciation dictionary.

        Args:
            value: String

        Returns:
            Number of the syllables in the word
        """
        if value in syllable_dict:
            # There are multiple pronounciation options in the CMU dictionary, here'
            # we'll just pick the first one
            phones = syllable_dict[value][0]
            return len([phone for phone in phones if self._is_vowel(phone)])
        return 0

    def _count_syllables_in_line(self, line):
        syllable_count = 0
        line = word_tokenize(line)
        for token in line:
            syllable_count += self._count_syllables_in_token(token)
        return syllable_count

    def _is_vowel(self, phone):
        """Check whether a phoneme from the CMU dictionary represents a vowel."""
        return any(c.isdigit() for c in phone)

    def _is_valid_token(self, token, remaining_syllables):
        allowed_excpetions = ["n't", ",", "-"]
        syllables = self.syllable_limits[self._line]
        stop_words = set(stopwords.words('english'))
        if remaining_syllables == syllables and not token.isalpha():
            return False
        if self._line == 3 and remaining_syllables == 1 and token in stop_words:
            return False
        if token in allowed_excpetions and (self._line < 3 or remaining_syllables > 1):
            return True
        return (token in syllable_dict and
                self._count_syllables_in_token(token) <= remaining_syllables)

    def _is_valid_haiku(self, haiku):
        haiku_lines = haiku.split("\n")
        if len(haiku_lines) != 3:
            return False
        for index, line in enumerate(haiku_lines, start=1):
            syllable_count = self._count_syllables_in_line(line)
            if syllable_count != self.syllable_limits[index]:
                return False
        return True

    def get_values_and_weights(self, nodes):
        values = [node.value for node in nodes]
        weights = [node.count for node in nodes]
        return (values, weights)

    def get_formatted_haiku(self, haiku):
        haiku = haiku.capitalize()
        haiku = haiku.replace(" i ", " I ")
        return haiku
