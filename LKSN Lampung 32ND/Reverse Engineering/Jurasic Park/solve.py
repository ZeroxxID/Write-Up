from Crypto.Util.number import *

# Diberikan nilai pada soal
p1 = 294704857459121458995842604700946850751
p2 = 314052721216923470597325825556277950411
res = 54846125195579777053464962994274277267744411269096779149171289487630586305476
e = 65537
flag = 4830690556514140397518897252109979335664677923435018942901273242454015697691068037340554551586759138432178879438287937684165299693520135533018994309974094302098369656069901396834

# Hitung nilai n (modulus)
n = p1 * p2

# Hitung nilai phi(n)
phi_n = (p1 - 1) * (p2 - 1)

# Hitung nilai d (private key exponent)
d = inverse(e, phi_n)

# Dekripsi nilai res untuk mendapatkan hr
hr = pow(res, d, n)

# Lakukan XOR antara hr dan flag
decrypted_flag = hr ^ flag

# Konversi hasil XOR ke teks (jika bisa)
result_text = decrypted_flag.to_bytes((decrypted_flag.bit_length() + 7) // 8, 'big').decode('utf-8')
print("Flag:", result_text)
