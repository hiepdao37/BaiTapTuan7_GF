
# Bai tap tuan 7 - Phep nhan da thuc trong GF(2^4) va GF(2^8)

## 1. Muc tieu
Cai dat thuat toan nhan hai phan tu trong truong huu han
GF(2^4) va GF(2^8) bang Python.

## 2. Bieu dien da thuc
Moi da thuc duoc bieu dien bang mot so nguyen.
Bit thu i la he so cua x^i.

Phep cong da thuc duoc thuc hien bang XOR.

## 3. Da thuc toi gian

- GF(2^4): p(x) = x^4 + x + 1, ma nhi phan 10011, hex 0x13.
- GF(2^8): p(x) = x^8 + x^4 + x^3 + x + 1,
  ma nhi phan 100011011, hex 0x11B.

## 4. Thuat toan
1. Khoi tao result = 0.
2. Neu bit thap nhat cua b la 1, result = result XOR a.
3. Dich b sang phai mot bit va a sang trai mot bit.
4. Neu a co so hang x^m, rut gon a bang XOR voi da thuc toi gian.
5. Lap lai den khi b = 0.

## 5. Cau truc du an
- gf.py: cai dat thuat toan nhan.
- main.py: chuong trinh minh hoa.
- tests/test_gf.py: bo kiem thu tu dong.

## 6. Cach chay
Chay chuong trinh:

    python3 main.py

Chay kiem thu:

    python3 -m unittest discover -s tests -v

## 7. Ket qua minh hoa
- GF(2^4): 0x7 * 0xB = 0x4
- GF(2^8): 0x57 * 0x83 = 0xC1

## 8. Ket luan
Chuong trinh cai dat phep nhan da thuc trong hai truong
GF(2^4) va GF(2^8), co rut gon theo da thuc toi gian
va co bo kiem thu cac truong hop co ban.
