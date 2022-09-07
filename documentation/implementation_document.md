# Implementation Document

## Structure

**Node**     
A building block for the trie structure. Each node represents one token, which has a value and a count. 
A token can be a complete word or some other accepted token (certain punctuation, tokenized suffixes etc.) The children of each node
are stored in a dictionary.

**Trie**    
The data structure, which is used for storing the input data. Enables inserting and searching sequences of tokens. Consist of Node objects.

**InputProcessor**     
Responsible for reading and preprocessing the input text to a form, where it can be saved to a trie. Uses `nltk.tokenize` for tokenization.

**HaikuGenerator**     
The main class responsible for haiku generation and validation. 

###

## Performance and Time and Space Complexity

The more detailed description on how the program performs can be found from the [testing document](./test_documentation.md). In a nutshell, using larger input files results in more unique outputs, whereas using smaller inputs often tend to generate results that repeat the source file, especially when using a higher order for the Markov chain. With highger orders the structure and grammar quality are usually a bit better, but there's usually less differences compared to the source text.

The time complexity of building the trie is O(nm), where n is the segment length and m is the number of distinct tokens. The time complexity for searching a segment from the trie is O(n), where n is the segment length.

The space complexity of the trie is O(nmw) where n is the depth of the trie (Markov chain order +1), m is the number of different n-length sequences in the trie, and where w is the number of distinct tokens in the source text.

## Deficiencies and Ideas for Improvements

There are still quite a lot of room for improvements, especially grammarwise. In many cases the haiku starts kind of mid-sentence - although poetry is in this sense maybe a bit more forgiving form of text, since the sentence structure isn't maybe as strict. Adjusting the possible start words for the haiku might help to solve the structure and grammar related issues, also speech tagging, lemmatization and stemming might be considered for improving the results.

In the future the program could be expanded for other languages as well - this would basically require only creating the syllable logic for each new language added. I was also planning on adding a theme/keyword selection, where the user could input a word of their choosing: in case where the given word is found in the trie it would be set as the start word, otherwise we could search the trie for possible synonyms (using WordNet) to be used as the start word. Unfortunately I didn't have time to finish this feature, so it was left out of the final version.

