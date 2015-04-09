"""
test compress
"""

import unittest

from compress import Compress

class TestCompress(unittest.TestCase):
    def setUp(self):
        self.c = Compress()

    def test_encode_word_the(self):
        enc = self.c.encode_symbol('the')
        binary = int(enc, 2)
        self.assertEquals(binary, 19)

    def test_encode_word_from(self):
        enc = self.c.encode_symbol('from')
        binary = int(enc, 2)
        self.assertEquals(binary, 109)

    def test_encode_word_home(self):
        enc = self.c.encode_symbol('home')
        binary = int(enc, 2)
        self.assertEquals(binary, 233)

    def test_encode_nonexistent_word(self):
        enc = self.c.encode_symbol('no-such-word')
        self.assertEquals(None, enc)

    def test_encode_char_space(self):
        enc = self.c.encode_symbol(' ')
        binary = int(enc, 2)
        self.assertEquals(binary, 7)

    def test_encode_char_e(self):
        enc = self.c.encode_symbol('e')
        binary = int(enc, 2)
        self.assertEquals(binary, 2)

    def test_encode_char_w(self):
        enc = self.c.encode_symbol('w')
        binary = int(enc, 2)
        self.assertEquals(binary, 48)

    def test_encode_text(self):
        enc = self.c.encode('this is')
        binary = int(enc, 2)
        self.assertEquals(binary, 183)

    def test_encode_text_with_punctuation(self):
        enc = self.c.encode('foo? is this bar!')
        binary = int(enc, 2)
        self.assertEquals(binary, 29686222816609210748006L)

    def test_encode_decode_1(self):
        s = 'you are really cool!'
        enc = self.c.encode(s)
        dec = self.c.decode(enc)
        self.assertEquals(s, dec)

    def test_encode_decode_2(self):
        s = '? i wonder how . compressed it ! will, be !'
        enc = self.c.encode(s)
        dec = self.c.decode(enc)
        self.assertEquals(s, dec)

    def test_encode_decode_3(self):
        s = 'xaajj tiko ax auui ahj nn nana nib'
        enc = self.c.encode(s)
        dec = self.c.decode(enc)
        self.assertEquals(s, dec)
