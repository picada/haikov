from input_processor import InputProcessor
from trie import Trie


class UI:
    def __init__(self):
        self.input_processor = InputProcessor()

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
                self.input_processor.read_and_preprocess_input("data/test.txt")
                continue
            if command == "2":
                tokenized_input = self.input_processor.read_and_preprocess_input("data/test.txt")
                trie = Trie(tokenized_input, 2)
                trie.create_trie()
                trie.print_trie()
                continue

    def _print_menu(self):
        """Prints the main menu with available selections
        """
        print(f"""
----------------------
        
*** Haikov ***

Main menu

1 - Test file reading (from a preset test file)
2 - Create and print the trie created from the input
0 - Quit

-----------------------

""")
