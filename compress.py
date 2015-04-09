"""
compression
"""

import Queue as queue

import random

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

    def __repr__(self):
        return "("+self.symbol+", "+str(self.freq)+")"

class Compress:
    """Compress"""
    def __init__(self):
        self.bits_to_symbol = {}
        self.symbol_to_bits = {}

        words = self.read_word_list()
        nodes = self.make_word_nodes(words)
        tree = self.build_huffman_tree(nodes)
        self.build_symbol_map('1', tree)

        nodes2 = self.make_char_nodes()
        tree2 = self.build_huffman_tree(nodes2)
        self.build_symbol_map('0', tree2)

    def make_char_nodes(self):
        chars = [(' ', 18.28), ('e', 10.26),
                ('t', 7.5), ('a', 6.5),
                ('o', 6.16), ('n', 5.7),
                ('i', 5.6), ('s', 5.3),
                ('r', 4.9), ('h', 4.8),
                ('l', 3.3), ('d', 3.28),
                ('u', 2.27), ('c', 2.23),
                ('m', 2.0), ('f', 1.9),
                ('w', 1.7), ('g', 1.6),
                ('p', 1.5), ('y', 1.4),
                ('b', 1.25), ('v', 0.79),
                ('k', 0.56), ('x', 0.14),
                ('j', 0.09), ('q', 0.08),
                ('z', 0.05), ('.', 0.04),
                (',', 0.039), ('?', 0.038),
                ('!', 0.037)]
        nodes = []
        for char in chars:
            node = HuffmanNode(char[0], char[1])
            nodes.append(node)
        return nodes

    def read_word_list(self):
        wordfile = open('words10000.txt', 'r')
        word_list = []
        for line in wordfile.readlines():
            word_list.append(line.strip() + ' ')
        wordfile.close()
        return word_list

    def make_word_nodes(self, words):
        fake_freq = 0.5
        nodes = []
        for word in words:
            node = HuffmanNode(word, fake_freq)
            fake_freq = fake_freq * 0.95
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
        symb = self.symbol_to_bits.get(string)
        if symb:
            return symb
        return self.symbol_to_bits.get(string + ' ')

    def decode_symbol(self, bits):
        """Decodes these bits if it is in the tree"""
        return self.bits_to_symbol.get(bits)

    def encode(self, string):
        """Encodes string to byte representation"""
        bitstring = ''

        for symbol in string.split(' '):
            symbol = symbol + ' '
            encoding = self.encode_symbol(symbol)
            if encoding == None:
                for s in symbol:
                    encoding = self.encode_symbol(s)
                    if encoding == None:
                        print "Skipping symbol: " + s
                    else:
                        bitstring += encoding
            else:
                bitstring += encoding

        l = len(self.encode_symbol(' '))
        return bitstring[:-l]

    def decode(self, byteString):
        """Decodes bytes into a text string"""
        decoded = ''
        portion_left = byteString
        while len(portion_left) > 0:
            substr_len = 1
            symbol = None
            while (symbol == None) and (substr_len <= len(portion_left)):
                symbol = self.decode_symbol(portion_left[:substr_len])
                substr_len += 1

            if symbol == None:
                print "decode failed:"
                print "decoded: " + decoded
                print "left: " + portion_left
                return None

            decoded += symbol
            #print "decoded: _" + symbol + "_"
            portion_left = portion_left[substr_len-1:]

        return decoded

def take_a_bit():
    if random.random() < 0.5:
        return '0'
    else:
        return '1'

def take_n_bits(n):
    bits = ''
    for i in range(n):
        bits += take_a_bit()
    return bits

if __name__ == '__main__':
    c = Compress()
    enc = c.encode('this is an example of huffman')
    dec = c.decode(enc)
    print dec

    print "#######"

    bits1 = take_n_bits(500)
    print c.decode(bits1)
