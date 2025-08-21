import base64

ords = "d3BqdkpBTXtqaGx6aHlfazNqeTl3YTNrX2xoNjBsMDBpfQ==" # Dữ liệu đã mã hóa từ hex sang bytes bằng base64

print(base64.b64encode(bytes.fromhex(ords)).decode()) # Giải mã từ base64 sang bytes và in ra