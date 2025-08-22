# Nghịch đảo modulo d = g^p-2
# Dạng 3*d = 1 (mod p)

g = int(input())
p = int(input())
d = pow(g, p - 2, p)

print(d)