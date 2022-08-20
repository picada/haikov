import os
from haiku_generator import HaikuGenerator
from input_processor import InputProcessor


class UI:
    def __init__(self):
        self._input_file = ""
        self._directory = "./data"
        self._input_processor = InputProcessor()

        self.data = ""
        self.haiku_generator = HaikuGenerator()

    def launch(self):
        """Loop for the main UI, called when launching the program
        """
        while(True):
            self._print_menu()
            command = input("Select next action: ")
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
                self._select_chain_order()
                continue
            if command == "4":
                self._generate_haiku()
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
            self.data = self._input_processor.read_and_preprocess_input(
                f"{self._directory}/{self._input_file}")
            self.haiku_generator.trie.create_trie(self.data)
        else:
            print("Invalid selection.")

    def _select_chain_order(self):
        selection = (input("Enter chain order: ",))
        if selection.isdigit():
            self.haiku_generator.change_degree(int(selection))
            self.haiku_generator.trie.create_trie(self.data)
            print(self.haiku_generator._degree)
            print(self.haiku_generator.trie.depth)
        else:
            print("Invalid selection.")

    def _generate_haiku(self):
        while(True):
            try:
                haiku = self.haiku_generator.attempt_haiku_generation()
                print("-----------------------", end="\n\n")
                print("Generated haiku:", end="\n\n")
                print(haiku, end="\n\n")
                print("-----------------------", end="\n\n")
            except Exception as exception:
                print(exception)
            print("<enter> - New haiku\n0 - Return to main menu\n")
            command = input("Select next action: ")
            print(command)
            if command == "0":
                break


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
Current Markov chain order: {self.haiku_generator._degree}
        
1 - Select new input file
2 - Print the trie created from the current input file
3 - Change Markov chain order
4 - Generate a haiku based on the current input file"""
