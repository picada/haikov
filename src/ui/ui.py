from haiku_generator import HaikuGenerator
from input_processor import InputProcessor
from trie import Trie


class UI:
    def __init__(self):
        self.input_processor = InputProcessor()
        self.trie = Trie()
        self.degree = 2
        self.tokenized_input = self.input_processor.read_and_preprocess_input(
            "data/trees_and_other_poems_joyce_kilmer.txt")

        self.trie = Trie(self.tokenized_input, self.degree+1)
        self.trie.create_trie()

        self.haiku_generator = HaikuGenerator(self.trie, self.degree)

    def launch(self):
        """Loop for the main UI, called when launching the program
        """
        while(True):
            self._print_menu()
            command = input()
            if command == "0":
                print("Bye!")
                break
            if command == "1":
                self.input_processor.read_and_preprocess_input(
                    "data/test.txt")
                continue
            if command == "2":
                self.trie.print_trie()
                continue
            if command == "3":
                try:
                    haiku = self.haiku_generator.attempt_haiku_generation()
                    print(haiku)
                except Exception as exception:
                    print(exception)
                continue

    def _print_menu(self):
        """Prints the main menu with available selections
        """
        print(f"""
----------------------
        
*** Haikov ***

Main menu

1 - Test file reading (from a preset test file)
2 - Print the trie created from the (preset) input file
3 - Generate a haiku based on the (preset) input file
0 - Quit

-----------------------

""")
