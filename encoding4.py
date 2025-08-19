from Crypto.Util.number import bytes_to_long, long_to_bytes

ords = 11515195063862318899931685488813747395775516287289682636499965282714637259206269 # Dữ liệu đã mã hóa từ bytes sang long

print(long_to_bytes(ords).decode()) # Giải mã từ long sang bytes và in ra
