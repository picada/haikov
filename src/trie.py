from node import Node

class Trie:
    def __init__(self, input_text="", depth=0):
        self.depth = depth
        self.root = Node()
        self.input_text = input_text

    def _reset(self):
        """Resets the root node to an empty node
        """
        self.root = Node()

    def create_trie(self):
        """Creates a new trie structure based on the input_textand defined depth.
        """
        self._reset()
        for sentence in self.input_text:
            for i in range(len(sentence) - (self.depth-1)):
                self._add_segment(sentence[i:i+self.depth])

    def _add_segment(self, segment):
        """Adds a new segment to the trie
        """
        current_node = self.root
        for token in segment:
            child = current_node.find_child(token)
            if not child:
                child = current_node.add_child(token)
                current_node = child
            else:
                child.count += 1
                current_node = child

    def find_segment(self, segment):
        """Checks if the given segment exists in the trie

        Args:
            segment: collection of tokens to be searched from the trie

        Returns:
            The the node for the last token in the segment if found
            None if segment is not found in the trie

        """
        node = self.root
        for token in segment:
            child = node.find_child(token)
            if not child:
                return None
            node = child
        return node

    def print_trie(self):
        """Prints the trie in a string form
        """
        self.root.print_children()
