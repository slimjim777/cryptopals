import unittest
from unittest import TestCase
from set1.challenge1 import hex_to_base64
from set1.challenge2 import fixed_xor


class Test(TestCase):
    def test_hex_to_base64(self):
        hex_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
        expected = b'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

        result = hex_to_base64(hex_string)
        self.assertEqual(expected, result)

    def test_fixed_xor(self):
        input1 = "1c0111001f010100061a024b53535009181c"
        input2 = "686974207468652062756c6c277320657965"
        expected = "746865206b696420646f6e277420706c6179"

        result = fixed_xor(input1, input2)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
