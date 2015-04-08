"""
compression
"""

import Queue as queue

class HuffmanNode:
    """Node in the Huffman coding tree"""
    def __init__(self, symbol, freq):
        self.parent = None
        self.children = []

        self.symbol = symbol
        self.freq = freq

    def set_parent(self, node):
        node.add_child(self)
        self.parent = node

    def add_child(self, node):
        self.children.append(node)

    def is_leaf(self):
        return len(self.children) == 0

class Compress:
    """Compress"""
    def __init__(self):
        self.word_list = []
        self.huffman_tree = None

        self.codeWordlist()
        self.build_huffman_tree()

    def codeWordlist(self):
        wordfile = open('words256.txt', 'r')
        for line in wordfile.readlines():
            self.word_list.append(line.strip())
        wordfile.close()

    def build_huffman_tree(self):
        fake_freq = 0.5
        nodes = []
        for word in self.word_list:
            node = HuffmanNode(word, fake_freq)
            fake_freq *= fake_freq
            nodes.append(node)

        priorityq = queue.PriorityQueue()
        for node in nodes:
            priorityq.put((node.freq, node))

        while(priorityq.qsize() > 1):
            n1 = priorityq.get()[1]
            n2 = priorityq.get()[1]
            parent = HuffmanNode("", n1.freq + n2.freq)
            n1.set_parent(parent)
            n2.set_parent(parent)
            priorityq.put((parent.freq, parent))

        self.huffman_tree = priorityq.get()[1]

    def encode(self, string):
        """Encodes string to byte representation"""
        return b'0'

    def decode(self, byteString):
        """Decodes bytes into a text string"""
        return ""

if __name__ == '__main__':
    c = Compress()
