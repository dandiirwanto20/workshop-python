# **Langkah 4. Jalankan kode**

# 1. Setel DATABASE_URL variabel lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda:

# $ export DATABASE_URL="{connection-string}"

# Di mana {connection-string}string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

# Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

# Jalankan kode:

# $ cd hello-world-python-psycopg2

# $ python example.py

# Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:

"""
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
"""
