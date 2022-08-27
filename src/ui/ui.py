import os
from services.haiku_generator import HaikuGenerator
from services.input_processor import InputProcessor


class UI:
    "Class for the UI"

    def __init__(self):
        """Constructor for the class. Initializes the input directory, input file and data,
        input processor and haiku generator.
        """
        self._directory = "./data"
        self._input_file = ""
        self._input_processor = InputProcessor()

        self.data = ""
        self.haiku_generator = HaikuGenerator()

    def launch(self):
        """Loop for the main UI, called from index.py when launching the program
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
        """Lists the available files in /data folder in the UI and let's
        the user choose a new input file from the available selections.
        Processes the chosen file and recreates the trie.
        """
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
        """Allows the user to change the current Markova chain order. Recreates the trie
        based on the given order.
        """
        selection = (input("Enter chain order: ",))
        if selection.isdigit():
            self.haiku_generator.change_degree(int(selection))
            self.haiku_generator.trie.create_trie(self.data)
        else:
            print("Invalid selection.")

    def _generate_haiku(self):
        """Calls the haiku genereator in order to create a new haiku. If succesful,
        prints out the generated haiku. If not, prints out an error message. Stays in the
        generation loop until 0 is entered.
        """
        while(True):
            try:
                haiku = self.haiku_generator.attempt_haiku_generation()
                self._print_haiku(haiku)
            except Exception as exception:
                print(exception)
            print("<enter> - New haiku\n0 - Return to main menu\n")
            command = input("Select next action: ")
            if command == "0":
                break

    def _print_haiku(self, haiku):
        print(
            f"""\
-----------------------

Generated haiku:

{haiku}

-----------------------
""")

    def _print_menu(self):
        """Prints the main menu with available selections
        """
        print(
            f"""\
----------------------
        
*** Haikov ***

Main menu

{self._get_available_menu_selections()}

-----------------------

""")

    def _get_available_menu_selections(self):
        if self._input_file == "":
            return \
                """\
1 - Select input file
0 - Quit
"""
        return \
            f"""\
Current input file: {self._input_file}
Current Markov chain order: {self.haiku_generator._degree}
        
1 - Select new input file
2 - Print the trie created from the current input file
3 - Change Markov chain order
4 - Generate a haiku based on the current input file
0 - Quit
"""
