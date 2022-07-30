class InputProcessor:
    def __init__(self):
        self.content = None

    def read_file(self, input_file):
        print(f"Reading file '{input_file}'.")

        try:
            with open(input_file, "r", encoding="utf-8") as file:
                content = file.read()
                self.content = content
            file.close()
        except IOError:
            print(f"Failed to read file '{input_file}'.")
