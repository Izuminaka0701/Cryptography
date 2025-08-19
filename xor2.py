# def xor(a, b):
#     return bytes(x ^ y for x, y in zip(a, b))

# KEY1 = bytes.fromhex("a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313") # Dữ liệu đã mã hóa từ hex sang bytes suwr dungj XOR
# xor1 = bytes.fromhex("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e") # Dữ liệu đã mã hóa từ hex sang bytes suwr dungj XOR
# xor2 = bytes.fromhex("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1") # Dữ liệu đã mã hóa từ hex sang bytes suwr dungj XOR
# xor3 = bytes.fromhex("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf") # Dữ liệu đã mã hóa từ hex sang bytes suwr dungj XOR


# print((xor(xor3, xor(KEY1, xor(xor(KEY1, xor1), xor(xor(KEY1, xor1), xor2))))).decode())# Giải mã bằng XOR


from pwn import xor
k1=bytes.fromhex('a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313')
k2_3=bytes.fromhex('c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1')
flag=bytes.fromhex('04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf')
print(xor(k1,k2_3,flag))  