
import sys
import unittest
from pathlib import Path

# Cho phép file test tìm thấy gf.py ở thư mục cha.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from gf import gf4_multiply, gf8_multiply


class TestGF4(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(gf4_multiply(0, 7), 0)

    def test_identity(self):
        for a in range(16):
            self.assertEqual(gf4_multiply(a, 1), a)

    def test_known_results(self):
        self.assertEqual(gf4_multiply(0x3, 0x5), 0xF)
        self.assertEqual(gf4_multiply(0x7, 0xB), 0x4)

    def test_commutative(self):
        for a in range(16):
            for b in range(16):
                self.assertEqual(
                    gf4_multiply(a, b),
                    gf4_multiply(b, a),
                )


class TestGF8(unittest.TestCase):
    def test_zero(self):
        self.assertEqual(gf8_multiply(0, 0x57), 0)

    def test_identity(self):
        for a in range(256):
            self.assertEqual(gf8_multiply(a, 1), a)

    def test_aes_known_result(self):
        # Kết quả chuẩn: 0x57 * 0x83 = 0xC1 với modulus 0x11B.
        self.assertEqual(gf8_multiply(0x57, 0x83), 0xC1)

    def test_commutative(self):
        for a, b in [(0x12, 0x34), (0xFF, 0xA5), (0x80, 0x02)]:
            self.assertEqual(
                gf8_multiply(a, b),
                gf8_multiply(b, a),
            )


if __name__ == "__main__":
    unittest.main()
