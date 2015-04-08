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

