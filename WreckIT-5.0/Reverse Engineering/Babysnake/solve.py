from base64 import b64encode as b64e, b64decode as b64d
 
def reverse_xor(apatuh):
    original = []
    for i, val in enumerate(apatuh):
        shifted = val >> i % 8 | val << (8 - i % 8)
        original_byte = (shifted & 255) ^ i
        original.append(original_byte)
    return bytes(original)
 
# Array target
apatuh = [87, 166, 29, 2, 244, 137, 148, 25, 56, 228, 161, 249, 230, 142, 
          84, 191, 105, 202, 233, 25, 167, 73, 93, 147, 117, 210, 172, 
          187, 151, 47, 80, 62, 16, 138, 68, 242]
 
# Mendapatkan input asli yang di-XOR
original_bytes = reverse_xor(apatuh)
 
# Periksa apakah panjang data valid untuk Base64 decoding
while len(original_bytes) % 4 != 0:
    original_bytes += b"="
 
# Decode dari Base64 untuk mendapatkan input asli
try:
    original_input = b64d(original_bytes).decode()
    print(f"Original input: {original_input}")
except Exception as e:
    print(f"Error decoding base64: {e}")
    print(f"Original bytes: {original_bytes}")
