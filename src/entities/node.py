class Node:
    def __init__(self, token=""):
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
        """
        for token, node in self.children.items():
            print(indent + str(token + ":" + str(node.count)))
            node.print_children(indent + "  ")
