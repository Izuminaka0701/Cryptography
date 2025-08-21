from pwn import xor

ords = b"label" # Mã hóa bằng XOR

# print("".join(chr(ord(c) ^ 13) for c in ords)) # max hóa từ bằng xor

print(xor(ords, 13)) # Giải mã bằng XOR với khóa 13