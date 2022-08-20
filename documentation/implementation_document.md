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
The main class responsible for haiku generation and validation. (Note: might still split this class up so, that the validation 
logic is in a separate class)

###

## Performance

## Time and Space Complexity

## Deficiencies and Ideas for Improvements

## Sources
