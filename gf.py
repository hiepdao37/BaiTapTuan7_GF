
"""Phép toán nhân trong GF(2^m).

Biểu diễn đa thức bằng số nguyên:
bit i là hệ số của x^i.
"""

GF4_M = 4
GF4_POLY = 0x13    # x^4 + x + 1

GF8_M = 8
GF8_POLY = 0x11B   # x^8 + x^4 + x^3 + x + 1


def gf_multiply(a: int, b: int, m: int, modulus: int) -> int:
    """Nhân a và b trong GF(2^m), rút gọn theo modulus."""
    if m < 1:
        raise ValueError("m phải lớn hơn hoặc bằng 1")
    if modulus < (1 << m):
        raise ValueError("Đa thức tối giản phải có bậc m")
    if not (0 <= a < (1 << m) and 0 <= b < (1 << m)):
        raise ValueError(f"a và b phải thuộc khoảng 0..{(1 << m) - 1}")

    result = 0
    high_bit = 1 << m

    while b:
        # Nếu bit thấp nhất của b bằng 1, cộng bằng XOR.
        if b & 1:
            result ^= a

        b >>= 1
        a <<= 1

        # Nếu xuất hiện x^m, rút gọn theo đa thức modulus.
        if a & high_bit:
            a ^= modulus

    return result


def gf4_multiply(a: int, b: int) -> int:
    """Nhân hai phần tử trong GF(2^4)."""
    return gf_multiply(a, b, GF4_M, GF4_POLY)


def gf8_multiply(a: int, b: int) -> int:
    """Nhân hai phần tử trong GF(2^8)."""
    return gf_multiply(a, b, GF8_M, GF8_POLY)
