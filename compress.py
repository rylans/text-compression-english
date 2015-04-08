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
        #self.word_tree= None
        #self.char_tree = None

        self.bits_to_symbol = {}
        self.symbol_to_bits = {}

        words = self.codeWordlist()
        nodes = self.make_word_nodes(words)
        tree = self.build_huffman_tree(nodes)
        self.build_symbol_map('1', tree)

    def codeWordlist(self):
        wordfile = open('words256.txt', 'r')
        for line in wordfile.readlines():
            self.word_list.append(line.strip())
        wordfile.close()
        return self.word_list

    def make_word_nodes(self, words):
        fake_freq = 0.5
        nodes = []
        for word in words:
            node = HuffmanNode(word, fake_freq)
            fake_freq *= fake_freq
            nodes.append(node)
        return nodes


    def build_huffman_tree(self, nodes):
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

        return priorityq.get()[1]

    def build_symbol_map(self, bit, root):
        self.build_symbol_map_recur(bit, root)

    def build_symbol_map_recur(self, bits, node):
        if node.is_leaf():
            self.bits_to_symbol[bits] = node.symbol
            self.symbol_to_bits[node.symbol] = bits
        else:
            lchild = node.children[0]
            rchild = node.children[1]
            self.build_symbol_map_recur(bits + '0', lchild)
            self.build_symbol_map_recur(bits + '1', rchild)

    def encode_symbol(self, string):
        """Encodes this string if it is in the tree"""
        return self.symbol_to_bits[string]

    def encode(self, string):
        """Encodes string to byte representation"""
        return b'0'

    def decode(self, byteString):
        """Decodes bytes into a text string"""
        return ""

if __name__ == '__main__':
    c = Compress()
    print c.symbol_to_bits
