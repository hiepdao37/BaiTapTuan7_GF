# Bài tập tuần 7: Nhân đa thức trong GF(2⁴) và GF(2⁸)

## 1. Mục tiêu
Cài đặt thuật toán nhân hai phần tử trong trường hữu hạn GF(2⁴) và GF(2⁸) bằng Python.

## 2. Biểu diễn đa thức
Mỗi đa thức được biểu diễn bằng một số nguyên, trong đó bit thứ i là hệ số của x^i.

Phép cộng đa thức được thực hiện bằng XOR.

## 3. Đa thức tối giản
- **GF(2⁴):** p(x) = x⁴ + x + 1, dạng hex `0x13`.
- **GF(2⁸):** p(x) = x⁸ + x⁴ + x³ + x + 1, dạng hex `0x11B`.

## 4. Thuật toán
1. Khởi tạo kết quả bằng 0.
2. Nếu bit thấp nhất của b bằng 1, XOR a vào kết quả.
3. Dịch b sang phải và nhân a với x bằng cách dịch trái.
4. Nếu bậc đa thức đạt m, rút gọn bằng XOR với đa thức tối giản.
5. Lặp đến khi b bằng 0.

## 5. Cấu trúc dự án
- `gf.py`: cài đặt phép nhân trong trường hữu hạn.
- `main.py`: chương trình minh họa.
- `tests/test_gf.py`: bộ kiểm thử tự động.

## 6. Cách chạy

Chạy chương trình:

```bash
python3 main.py
```

Chạy kiểm thử:

```bash
python3 -m unittest discover -s tests -v
```

## 7. Kết quả minh họa
- GF(2⁴): `0x7 * 0xB = 0x4`
- GF(2⁸): `0x57 * 0x83 = 0xC1`

## 8. Kết luận
Chương trình thực hiện phép nhân đa thức trong hai trường hữu hạn, rút gọn theo đa thức tối giản và kiểm tra kết quả bằng các trường hợp kiểm thử.
