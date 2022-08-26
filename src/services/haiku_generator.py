import random

import nltk
from nltk.corpus import cmudict, stopwords
from nltk.tokenize import word_tokenize

from entities.trie import Trie

nltk.download('cmudict')
nltk.download('stopwords')
syllable_dict = cmudict.dict()

MAX_ATTEMPTS = 100


class HaikuGenerator:
    def __init__(self, degree=2):
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
        remaining_syllables = syllable_limit - \
            self._count_syllables_in_line(line)

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
        if valid_choices:
            token = self.get_random_node(valid_choices.values()).value
            return token
        raise Exception(
            "Couldn't find valid choices for the next word.")

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
        """Counts the number of syllables in a line by counting the syllables of
        each token in the line and summing them up

        Args:
            line: String

        Returns:
            Number of the syllables in the given line
        """
        syllable_count = 0
        line = word_tokenize(line)
        for token in line:
            syllable_count += self._count_syllables_in_token(token)
        return syllable_count

    def _is_vowel(self, phone):
        """Check whether a phoneme from the CMU dictionary represents a vowel."""
        return any(c.isdigit() for c in phone)

    def _is_valid_token(self, token, remaining_syllables):
        """Checks if the given token is valid or not. A token is valid if:
        a) it's a complete word (all characters are alphabets) if it's in the beginning
           of a sentence
        b) it's not a stopword if it's in the end of the last line
        c) it's not one of the agreed expections (n't, , -) and it's not in the beginning or
           in the end of the haiku
        d) the token can be found from the cmu dictionary and the syllable count is less
           than the remaining syllables

        Args:
            token: String
            remaining_syllables: number

        Returns:
            True if the token is valid, otherwise False
        """
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
        """Checks if the given haiku is valid or not. A token is valid if:
        a) it has three lines AND
        b) each of the lines has the correct amount of syllables (defined in self.syllable_limits)

        Args:
            haiku: String

        Returns:
            True if the haiku is valid, otherwise False
        """
        haiku_lines = haiku.split("\n")
        if len(haiku_lines) != 3:
            return False
        for index, line in enumerate(haiku_lines, start=1):
            syllable_count = self._count_syllables_in_line(line)
            if syllable_count != self.syllable_limits[index]:
                return False
        return True

    def get_formatted_haiku(self, haiku):
        """Formats the final valid haiku by adding capitalization

        Args:
            haiku: String

        Returns:
            String
        """
        haiku = haiku.capitalize()
        haiku = haiku.replace(" i ", " I ")
        haiku = haiku.replace(" i\n", " I\n")
        haiku = haiku.replace("\ni ", "\nI ")
        return haiku

    def get_random_node(self, nodes):
        """Return a random node from the given list of nodes. The randomness
        is adjusted based on the weight (count) of the node

        Args:
            nodes: array of nodes

        Returns:
            Node object
        """
        weights = [node.count for node in nodes]
        total_weight = sum(weights)

        rnd = random.randint(1, total_weight)
        for node in nodes:
            rnd -= node.count
            if rnd <= 0:
                return node
        raise Exception("Unable to get random node.")

    def change_degree(self, degree):
        """Changes the degree of the generator and adjusts the depth of the trie
        accordingly
        """
        self._degree = degree
        self.trie.depth = degree + 1
