ords = "label" # Mã hóa bằng XOR

print("".join(chr(ord(c) ^ 13) for c in ords)) # max hóa từ bằng xor