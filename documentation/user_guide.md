# User guide

## Prequisities

You should have Python and Poetry installed in order to run the program. The program is developed using Python 3.8.5.

## Running the program

1. Clone the repository

2. Open the reporitory folder in terminal and install the dependencies by running

`poetry install`

3. After this, you can run the program by running

`poetry run invoke start`

## Using the program

When you start the program, you first encounter a menu with only two options:

<img width="492" alt="Screenshot 2022-08-20 at 19 16 38" src="https://user-images.githubusercontent.com/32310572/185756464-95c89b1f-3244-4ed5-b11a-3c0b8ef957a8.png">


Select 1 and press enter in order to proceed to input selection. 

<img width="448" alt="Screenshot 2022-08-20 at 19 06 41" src="https://user-images.githubusercontent.com/32310572/185756503-5b437ec9-7aea-4a46-8c4f-1ccc5cbf2a6a.png">


All the input files are located inside the [data](https://github.com/picada/haikov/tree/main/data) folder. There is a selection of preset input options, but you can also add your own input
to the folder. When adding new input files please note, that the file should be in `.txt` form and that currently the programs supports only
English texts.

When the input file is selected, the program creates the trie based on the input and the default Markov chain order (2), after which you'll be able to
access the main menu.

<img width="501" alt="Screenshot 2022-08-20 at 19 08 36" src="https://user-images.githubusercontent.com/32310572/185756518-7ed9b832-0d82-4095-8664-53c589e10a52.png">


Here you have a few options:

1 - Select new input file - opens the input selection menu     
2 - Print the trie created from the current input file - Prints a string representation of the trie structure to the terminal      
3 - Change Markov chain order - Changes the Markov order based on the input and updates the trie accordingly      
4 - Generate a haiku based on the current input file - Creates a haiku based on the current settings and prints it to the terminal. If a valid      
    haiku cannot be created with the given input and settings, and error message will appear instead      
0 - Quit

After generating a new haiku, you can either create a new one with the same settings by pressing enter, or return to the main menu with 0.

<img width="445" alt="Screenshot 2022-08-20 at 19 13 43" src="https://user-images.githubusercontent.com/32310572/185756443-4fa970b1-a23e-46f8-9a82-ddbd5c3f28da.png">
