import base64

ords = "72bca9b68fc16ac7beeb8f849dca1d8a783e8acf9679bf9269f7bf" # Dữ liệu đã mã hóa từ hex sang bytes bằng base64

print(base64.b64encode(bytes.fromhex(ords)).decode()) # Giải mã từ base64 sang bytes và in ra