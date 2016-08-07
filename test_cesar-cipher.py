from cesar_cipher import cesar_cipher
from unittest import TestCase

class TestCesarCipher(TestCase):

    def test_empty_to_word_returns_empty(self):
        self.assertEqual("", cesar_cipher("", 0), 'I expected a empty word')

    def test_a_to_returns_b(self):
        self.assertEqual("b", cesar_cipher("a", 1))

    def test_a_to_returns_c(self):
        self.assertEqual("c", cesar_cipher("a", 2))

    def test_ab_with_shift_1_to_returns_bc(self):
        self.assertEqual("bc", cesar_cipher("ab", 1))
