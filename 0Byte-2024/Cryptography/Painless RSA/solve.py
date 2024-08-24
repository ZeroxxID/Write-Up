def rsa_decrypt(ciphertext, d, n):
    # RSA decryption: m = c^d % n
    plaintext = pow(ciphertext, d, n)
    return plaintext

def int_to_ascii(value):
    # Mengubah integer ke ASCII jika memungkinkan
    result = ""
    while value > 0:
        result = chr(value % 256) + result
        value //= 256
    return result

# Given RSA private key (d) and modulus (n)
d = 3398532790434950753
n = 7677685062000954947

# List of ciphertext flags
flags = [
    2443137791084585392,
    1316897719607221125,
    4976310067108619182,
    3610829399007524213,
    6316574104951079329,
    3038443601564574614,
    1517623105423636182,
    206044343327838794,
    5662286151805572806,
    5632142875002422271,
    7488572422520737027,
    1701472596887842143,
    1940216855856806259,
    3823190890497686220,
    5296891837614609202
]

# Decrypt each flag and convert to ASCII
for i, flag in enumerate(flags, start=1):
    decrypted_value = rsa_decrypt(flag, d, n)
    ascii_value = int_to_ascii(decrypted_value)
    print(ascii_value, end='')
