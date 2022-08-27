import random


class Node:
    """The main building block in Trie, represents a token which has a value and a count (weight)
    """

    def __init__(self, token=""):
        """Constructor for the class. Initializes the token value and count (number of occurences)
        and an empty dictionary for the children.

        Args:
            token: String, value of the token
        """
        self.value = token
        self.count = 1
        self.children = {}

    def add_child(self, token):
        """Creates a new Node object and adds it to the children dictionary of
        the current node

        Args:
            token: String, a single word or a punctuation mark

        Returns:
            Node object
        """
        child_node = Node(token)
        self.children[token] = child_node
        return child_node

    def increment_count(self):
        """Increases the count (number of occurences) by one
        """
        self.count += 1

    def find_child(self, token):
        """Returns a child node, if it can be found from the children of the node based
        on the token

        Args:
            token: String, a single word or a punctuation mark

        Returns:
            Node object or None
        """
        if token in self.children:
            return self.children[token]
        return None

    def print_children(self, indent=""):
        """Prints the children of the current node to stdout

        Args:
            indent: String, indentation whitespace for the recursive function
        """
        for token, node in self.children.items():
            print(indent + str(token + ":" + str(node.count)))
            node.print_children(indent + "  ")

    @staticmethod
    def get_random_node(nodes):
        """Return a random node from the given list of nodes. The randomness
        is adjusted based on the weight (count) of the node

        Args:
            nodes: array of nodes

        Returns:
            Node object
        """
        weights = [node.count for node in nodes]
        total_weight = sum(weights)

        rnd = random.randint(1, total_weight)
        for node in nodes:
            rnd -= node.count
            if rnd <= 0:
                return node
        raise Exception("Unable to get random node.")
