# Kloning repo GitHub kode sampel:

# $ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2

# Kode sampel di example.pymelakukan hal berikut:

"""
 * Membuat accounts tabel dan menyisipkan beberapa baris
 * Mentransfer dana antara dua akun dalam suatu transaksi
 * Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali kode contoh
"""

"""
Untuk menangani kesalahan percobaan ulang transaksi, kode menggunakan pengulangan percobaan tingkat aplikasi yang, 
jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. 
Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan backoff eksponensial.
"""