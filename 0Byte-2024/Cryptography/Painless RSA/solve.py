from Crypto.Util.number import *

def rsa_decrypt(ciphertext, d, n):
    # RSA decryption: m = c^d % n
    plaintext = pow(ciphertext, d, n)
    return plaintext

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

# Looping decode 
for i in flags:
    decode = rsa_decrypt(i,d,n)
    print(long_to_bytes(decode).decode(),end='')
