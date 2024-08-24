# Given encrypted flag
enc = 232248373780702558559732705634320310324639111824357224567527709756665492238132012558072443413580231257415
 
# Function to decrypt the flag
def decrypt_flag(key_combination):
    key_sum = sum(key_combination)
    fint = enc // key_sum
    flag = bytes.fromhex(hex(fint)[2:]).decode()
    return flag
 
# Possible keys found
possible_keys = [
    (3, 14, 2),
    (4, 12, 3),
    (5, 10, 4),
    (6, 8, 5),
    (7, 6, 6),
    (8, 4, 7),
    (9, 2, 8),
    (10, 0, 9)
]
 
# Try decrypting with each possible key combination
for keys in possible_keys:
    try:
        flag = decrypt_flag(keys)
        if flag.startswith("WRECKIT50{"):
            print(f"Possible key: {keys}")
            print(f"Flag: {flag}")
            break
    except Exception as e:
        continue
