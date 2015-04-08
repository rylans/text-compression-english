"""
test compress
"""

import unittest

from compress import Compress

class TestCompress(unittest.TestCase):
    def test_encode_returns_bytes(self):
        c = Compress()
        enc =  c.encode('foo')
        self.assertTrue(isinstance(enc, bytes))

    def test_decode_returns_string(self):
        c = Compress()
        dec = c.decode(b'123')
        self.assertTrue(isinstance(dec, str))

