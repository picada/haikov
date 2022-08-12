import os
from haiku_generator import HaikuGenerator
from input_processor import InputProcessor


class UI:
    def __init__(self):
        self._input_file = ""
        self._directory = "./data"
        self._input_processor = InputProcessor()
        
        self.degree = 2
        self.haiku_generator = HaikuGenerator(self.degree)

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
                self._select_input()
                continue
            if command == "2":
                self.haiku_generator.trie.print_trie()
                continue
            if command == "3":
                try:
                    haiku = self.haiku_generator.attempt_haiku_generation()
                    print(haiku)
                except Exception as exception:
                    print(exception)
                continue

    def _select_input(self):
        file_names = os.listdir(self._directory)
        options = {}
        for index, file in enumerate(file_names, start=1):
            options[index] = file
        print("Available files:", end="\n\n")
        for key in options:
            print(f"""{key} - {options[key]}""")
        selection = (input("\nChoose input file: ",))
        if selection.isdigit() and int(selection) in [*options]:
            self._input_file = options[int(selection)]
            data = self._input_processor.read_and_preprocess_input(f"{self._directory}/{self._input_file}")
            self.haiku_generator.trie.create_trie(data)
        else:
            print("Invalid selection.")

# todo: clean up formatting in menu
    def _print_menu(self):
        """Prints the main menu with available selections
        """
        print(f"""
----------------------
        
*** Haikov ***

Main menu

{self._get_menu_selections()}
0 - Quit

-----------------------

""")

    def _get_menu_selections(self):
        if self._input_file == "":
            return "1 - Select input file"
        return f"""Current input file: {self._input_file}
        
1 - Select new input file
2 - Print the trie created from the current input file
3 - Generate a haiku based on the current input file"""
