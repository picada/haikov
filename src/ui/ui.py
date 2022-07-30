from input_processor import InputProcessor

class UI:
    def __init__(self):
        self.input_processor = InputProcessor()

    def launch(self):
        while(True):
            self._print_menu()
            command = input()
            if command == "0":
                print("Bye!")
                break
            if command == "1":
                self.input_processor.read_file("data/test.txt")
                print(f"Input:\n{self.input_processor.content}")
                continue

    def _print_menu(self):
        print(f"""
----------------------
        
*** Haikov ***

Main menu

1 - Test file reading (from a preset test file)
0 - Quit

-----------------------

""")
