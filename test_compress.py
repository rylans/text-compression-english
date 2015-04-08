"""
test compress
"""

import unittest

from compress import Compress

class TestCompress(unittest.TestCase):
    def setUp(self):
        self.c = Compress()

    def test_encode_returns_bytes(self):
        enc = self.c.encode('foo')
        self.assertTrue(isinstance(enc, bytes))

    def test_decode_returns_string(self):
        dec = self.c.decode(b'123')
        self.assertTrue(isinstance(dec, str))

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
