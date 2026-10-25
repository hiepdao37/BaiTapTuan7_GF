
from gf import gf4_multiply, gf8_multiply


def main():
    print("=== PHEP NHAN TRONG TRUONG HUU HAN ===")

    print("\n1. Truong GF(2^4)")
    a4 = 0x7
    b4 = 0xB
    r4 = gf4_multiply(a4, b4)
    print(f"{a4:#x} * {b4:#x} = {r4:#x}")

    print("\n2. Truong GF(2^8)")
    a8 = 0x57
    b8 = 0x83
    r8 = gf8_multiply(a8, b8)
    print(f"{a8:#x} * {b8:#x} = {r8:#x}")


if __name__ == "__main__":
    main()
