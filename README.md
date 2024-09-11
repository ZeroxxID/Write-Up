Modern cryptography involves code, and code involves coding. CryptoHack provides a good opportunity to sharpen your skills.<br>
Of all modern programming languages, Python 3 stands out as ideal for quickly writing cryptographic scripts and attacks. For more information about why we think Python is so great for this, please see the <a href="https://cryptohack.org/faq/#python3">FAQ</a>.<br>
Run the attached Python script and it will output your flag.<br>

Challenge files:
- <a href="https://cryptohack.org/static/challenges/great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py">great_snakes.py</a>

Resources:
 - <a href="https://wiki.python.org/moin/BeginnersGuide/Download">Downloading Python</a><br>

> Explanation Source Code: <br>
> Pada source code yang diberikan dapat dilihat variabel `ords` merupakan variabel yang berisikan value dalam bentuk array, jika diperhatikan itu bukan sembarang angka melainkan merupakan angka desimal.
> <br>
> Kita lanjut lihat baris paling terakhir `print("".join(chr(o ^ 0x32) for o in ords))`. Disini akan dijabarkan sejelas mungkin:
> - `print()` digunakan untuk menampilkan output `argument` dari `expression` yang terdapat didalam fungsi `print()`. Apa bedanya `argument`, `expresion`, dan `generator expression`? Oke, jadi untuk `generator expression` contoh disini `(chr(o ^ 0x32) for o in ords)`, `expresion` merupakan keseluruhan isi dalam fungsi `print()`contoh disini `"".join(chr(o ^ 0x32) for o in ords)`, kemudian hasil dari `expresion` tersebut disebut sebagai `argument` contoh disini  `"crypto{z3n_0f_pyth0n}"`.
> - `"".join()` berfungsi untuk menggabungkan dan menggubah elemen-elemen dari suatu iterable (seperti list, tuple, atau generator) menjadi satu string. Nantinya setiap karakter tersebut bakal disisipkan `""` hasilnya `crypto{z3n_0f_pyth0n}`, contoh lain `".".join()` maka hasilnya `c.r.y.p.t.o.{.z.3.n._.0.f._.p.y.t.h.0.n.}`.
> - `chr()` berfungsi sebagai pengubah desimal menjadi karakter/ASCII/Unicode. Dapat menggunakan hex juga `print(chr(0x32))` atau oktal `print(chr(0o101))` yang nantinya bakal diubah secara otomatis ke desimal.
> - `o` merupakan pemanggilan variabel yang dideklarasi dari fungsi for yang tertuju pada value variabel `ords`/iterabel. Iterable adalah objek dalam pemrograman yang dapat diulang (di-loop), artinya Anda bisa mengakses elemen-elemennya satu per satu. 
> - `^ 0x32` merupakan operator logika `XOR` yang dimana variabel `o` nanti nya akan melakukan `XOR` dengan hexadecimal `0x32`. Terus berapakah nilai desimal dari `0x32`? Mari gunakan python `print(int("0x32,16"))` maka akan menghasilkan `50`. Kita juga dapat melakukan `XOR` tanpa mengetahui berapakah desimalnya namun bukannya kita lebih baik mengetahuinya? Wkwkwk, jika kalian ingin langsung melakukan `XOR` bisa gunakan python `[Value dalam ords] ^ 0x32` atau dalam desimal `[Value dalam ords] ^ 50`.
> - `for o in ords` akan melakukan sebuah pengulangan hingga value array dalam `ords`/iterabel berakhir.
> <br>
> Oke untuk yang terakhir coba lihat output yang dihasilkan dari kedua program, berbeda bukan? Yang satu sebaris yang satu berbaris-baris wkwkwk. Hal ini dikarenakan semua karakter pada yang pertama digabung menjadi satu string terlebih dahulu oleh `"".join()`, kemudian seluruh string tersebut dicetak sekaligus dalam satu panggilan `print()` sedangkan yang kedua  setiap panggilan `print()` mencetak satu karakter pada baris baru, hal ini dikarenakan setiap iterasi memanggil fungsi `print()` yang menambahkan newline `\n` secara otomatis. Hal ini tentu membuat kesal namun solusinya menambahkan parameter `end=""` contoh `print(chr(number ^ 0x32), end="")`.<br><br>
> Solve: Run the file on python `python3 great_snakes_35381fca29d68d8f3f25c9fa0a9026fb.py`<br><br>
> Flag: `crypto{z3n_0f_pyth0n}`
 
