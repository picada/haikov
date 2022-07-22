# Requirement specification

**Documentation Language**: English

**Main Programming Language**: Python

**Other Languages for Peer Reviews**: I'll probably be able to review stuff made with Java as well if needed, although it's been quite long since I've last touched the language in any way

**Study program**: Bachelor's in Computer Science (Tietojenkäsittelytieteen kandidaatti)

## Subject:

The program is meant to take a text file as an input, and generate a valid haiku styled poem based on the source text as an output using Markov Chains. Haikus are short poems, that traditionally consist of three lines and 17 syllables, which are divided to the lines in a 5-7-5 pattern. There are also more specific rules to traditional haikus (for example a seasonal reference) which I do not dare promise to fulfill, hence the term 'haiku styled'.

The input file should be in English, as the syllable logic will be built based on the English language rules. In the future there could be a chance to expand the logic to other languages as well.

The input data will be saved to a trie data structure, and the program will be using Markov Chains for generating the haikus.

I am also planning on using NLTK (Natural Language Toolkit) for text preprocessing, and Project Gutenberg will be used as the main source for training data during the development.

## Sources
