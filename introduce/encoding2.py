ords = "63727970746f7b596f755f77696c6c5f62655f776f726b696e675f776974685f6865785f737472696e67735f615f6c6f747d" # Dữ liệu đã mã hóa từ hex


print("".join(chr(o) for o in bytes.fromhex(ords))) # Giải mã từ hex sang bytes và in ra cách 1

print(bytes.fromhex(ords).decode()) # Giải mã từ hex sang bytes và in ra cách 2