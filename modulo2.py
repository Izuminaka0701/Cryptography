# THuật toán Euclid mở rộng
def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0  # gcd(a,0) = a và nghiệm (x=1, y=0)
    else:
        g, x1, y1 = extended_euclid(b, a % b)
        # cập nhật x, y dựa trên kết quả đệ quy
        x = y1
        y = x1 - (a // b) * y1
        return g, x, y


# Ví dụ sử dụng
a, b = 26513, 32321
g, x, y = extended_euclid(a, b)

print(f"{x}, {y}")