# ords = "a35812c5d02a75842924ca1f013084ae950c5b308e841b79e69b462bdedb876b314ca7cbff4de228ee2ab49d7f8bb36c2ee3571aff9b7a07c9f1d6ee7222b5a8" # Dữ liệu đã mã hóa từ hex


# print("".join(chr(o) for o in bytes.fromhex(ords))) # Giải mã từ hex sang bytes và in ra cách 1

# print(bytes.fromhex(ords).decode()) # Giải mã từ hex sang bytes và in ra cách 2

# verify_ecdsa_raw.py
import binascii

# Original token
token = "0c38faaf4fb86ca7f9436bffa8e2651441b1da8b1934e3ddf04b0ec485660d8ee093ccfc65ba466962e5c809abf4d6c56650416699d11b19cbb0e71e18e1148ee0fa0a91c6f3b35ce58bb95017d64dfc08565f760773c933ceec5f91f032badfaa1c7415a9c56a280512a9d312105a4e"

# Convert hex to binary
binary = bytes.fromhex(token)

# Assume '0' in "is_admin":0 is in the last byte (byte 72)
# Modify the corresponding byte in the previous block (byte 56, assuming 16-byte blocks)
binary = list(binary)
binary[56] ^= 0x01  # Flip bit to change '0' to '1'
new_token = bytes(binary).hex()

print("Modified token:", new_token)

# Instructions to test:
# 1. Copy the modified token
# 2. Submit it to verify.php via POST:
#    curl -X POST -d "token=<new_token>" http://example.com/verify.php
# 3. Check the response for the FLAG

