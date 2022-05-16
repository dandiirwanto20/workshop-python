# **Langkah 4. Inisialisasi database**

# Setel DATABASE_URL variabel lingkungan ke string koneksi untuk cluster Anda:

# export DATABASE_URL="{connection-string}"

#Di mana {connection-string} string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

# Untuk menginisialisasi database contoh, gunakan cockroach sqlperintah untuk mengeksekusi pernyataan SQL dalam dbinit.sqlfile:

# $ cat dbinit.sql | cockroach sql --url $DATABASE_URL

# Pernyataan SQL dalam file inisialisasi harus dijalankan:

"""
CREATE TABLE

Time: 102ms
"""