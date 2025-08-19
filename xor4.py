cryp = bytes.fromhex("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104") # Mã hóa từ hex sang bytes


key = b"myXORkey" # Tính khóa bằng XOR với ký tự 'c'
print(''.join(chr(c ^ key[i % len(key)]) for i, c in enumerate(cryp))) # Giải mã
        