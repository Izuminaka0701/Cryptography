test1 = bytes.fromhex("73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d") # Dữ liệu đã mã hóa từ hex sang bytes 

for i in range(256): 
    result = ''.join(chr(c ^ i) for c in test1)
    if "crypto" in result:
        print(result)
        break