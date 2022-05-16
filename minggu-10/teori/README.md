# PEP 249 – Python Database API Specification v2.0

## Introduction

API ini telah didefinisikan untuk mendorong kesamaan antara modul Python yang digunakan untuk mengakses database. Dengan melakukan ini, kita berharap dapat mencapai konsistensi yang mengarah ke modul yang lebih mudah dipahami, kode yang umumnya lebih portibel di seluruh basis data, dan jangkauan konektivitas basis data yang lebih luas dari Python.

Pada Dokumentasi ini menjelaskan Spesifikasi Python database API 2.0 dan satu set ekstensi opsional umum. Penulis paket didorong untuk menggunakan versi spesifikasi ini sebagai dasar untuk antarmuka baru.

## Modul Interface

**Constructors**

Akses ke database tersedia melalui objek koneksi. Modul harus menyediakan konstruktor berikut untuk ini:

connect( parameters… )

Konstruktor untuk membuat koneksi ke database.
Mengembalikan Objek Koneksi . Dibutuhkan sejumlah parameter yang bergantung pada basis data.

**Global**

Global modul ini harus didefinisikan:
  * apilevel: Konstanta string yang menyatakan level DB API yang didukung. Saat ini hanya string `“ 1.0”` dan `“ 2.0”` yang diperbolehkan. Jika tidak diberikan, antarmuka level DB-API 1.0 harus diasumsikan.
  * threadsafety: Konstanta bilangan bulat yang menyatakan tingkat keamanan utas yang didukung antarmuka.
  * paramstyle: Konstanta string yang menyatakan jenis pemformatan penanda parameter yang diharapkan oleh antarmuka.

**Exceptions**

Modul harus membuat semua informasi kesalahan tersedia melalui pengecualian ini atau subkelasnya:
  * Warning: Pengecualian untuk peringatan penting seperti pemotongan data saat memasukkan, dll. Itu harus menjadi subkelas dari Python `StandardError` (didefinisikan dalam pengecualian modul).
  * Error: Pengecualian yang merupakan kelas dasar dari semua pengecualian kesalahan lainnya. Anda dapat menggunakan ini untuk menangkap semua kesalahan dengan satu exceptpernyataan tunggal. Peringatan tidak dianggap sebagai kesalahan dan karenanya tidak boleh menggunakan kelas ini sebagai basis. Itu harus menjadi subkelas dari Python `StandardError`(didefinisikan dalam pengecualian modul).
  * InterfaceError: Pengecualian dimunculkan untuk kesalahan yang terkait dengan antarmuka basis data daripada basis data itu sendiri. Itu harus menjadi subkelas dari Error.
  * DatabaseError: Pengecualian dimunculkan untuk kesalahan yang terkait dengan database. Itu harus menjadi subkelas dari Error.
  * DataError: Pengecualian untuk kesalahan yang disebabkan oleh masalah dengan data yang diproses seperti pembagian dengan nol, nilai numerik di luar jangkauan, dll. Itu harus merupakan subkelas dari `DatabaseError`.
  * OperationalError: Pengecualian untuk kesalahan yang terkait dengan operasi basis data dan tidak harus di bawah kendali pemrogram, misalnya terjadi pemutusan yang tidak terduga, nama sumber data tidak ditemukan, transaksi tidak dapat diproses, kesalahan alokasi memori terjadi selama pemrosesan, dll. Ini harus merupakan subkelas dari `DatabaseError`.
  * IntegrityError: Pengecualian muncul ketika integritas relasional database terpengaruh, misalnya pemeriksaan kunci asing gagal. Itu harus menjadi subkelas dari `DatabaseError`.
  * InternalError: Pengecualian muncul ketika database mengalami kesalahan internal, misalnya kursor tidak valid lagi, transaksi tidak sinkron, dll. Itu harus merupakan subkelas dari `DatabaseError`.
  * ProgrammingError: Pengecualian untuk kesalahan pemrograman, misalnya tabel tidak ditemukan atau sudah ada, kesalahan sintaks dalam pernyataan SQL, jumlah parameter yang salah ditentukan, dll. Itu harus merupakan subkelas dari `DatabaseError`.
  * NotSupportedError: Pengecualian muncul jika metode atau API database digunakan yang tidak didukung oleh database, misalnya meminta `.rollback()` pada koneksi yang tidak mendukung transaksi atau menonaktifkan transaksi. Itu harus menjadi subkelas dari `DatabaseError`.

## Connection Objects

## Connection methods

**.close()**

Tutup koneksi sekarang (bukan kapan pun `.__del__()` dipanggil). Sambungan tidak akan dapat digunakan mulai saat ini; pengecualian Kesalahan (atau subkelas) akan dimunculkan jika ada operasi yang dicoba dengan koneksi. Hal yang sama berlaku untuk semua objek kursor yang mencoba menggunakan koneksi. Perhatikan bahwa menutup koneksi tanpa melakukan perubahan terlebih dahulu akan menyebabkan rollback implisit dilakukan.

**.commit()**

Komit setiap transaksi yang tertunda ke database. Perhatikan bahwa jika database mendukung fitur komit otomatis, ini harus dimatikan terlebih dahulu. Metode antarmuka dapat disediakan untuk mengaktifkannya kembali. Modul database yang tidak mendukung transaksi harus mengimplementasikan metode ini dengan fungsionalitas batal.

**.rollback()**

Metode ini opsional karena tidak semua database menyediakan dukungan transaksi. Jika database menyediakan transaksi, metode ini menyebabkan database memutar kembali ke awal transaksi yang tertunda. Menutup koneksi tanpa melakukan perubahan terlebih dahulu akan menyebabkan rollback implisit dilakukan.

**.cursor()**

Kembalikan Objek Kursor baru menggunakan koneksi. Jika database tidak menyediakan konsep kursor langsung, modul harus mengemulasi kursor menggunakan cara lain sejauh yang dibutuhkan oleh spesifikasi ini. 

## Cursor Objects

Objek ini mewakili kursor database, yang digunakan untuk mengelola konteks operasi pengambilan. Kursor yang dibuat dari koneksi yang sama tidak terisolasi, yaitu , setiap perubahan yang dilakukan ke database oleh kursor akan segera terlihat oleh kursor lain. Kursor yang dibuat dari koneksi yang berbeda dapat atau tidak dapat diisolasi, tergantung pada bagaimana dukungan transaksi diimplementasikan (lihat juga metode `.rollback ()` dan `.commit ()` koneksi).

Objek Kursor harus merespons metode dan atribut berikut.

## Cursor attributes

**.description**

Atribut read-only ini adalah urutan dari urutan 7-item.

Masing-masing urutan ini berisi informasi yang menjelaskan satu kolom hasil:

* `name`
* `type_code`
* `display_size`
* `internal_size`
* `precision`
* `scale`
* `null_ok`

Dua item pertama ( `name` dan `type_code`) adalah wajib, lima lainnya opsional dan disetel ke `None` jika tidak ada nilai bermakna yang dapat diberikan.

Atribut ini akan digunakan `None` untuk operasi yang tidak mengembalikan baris atau jika kursor belum memiliki operasi yang dipanggil melalui metode `.execute*()`.

The `type_code` dapat diinterpretasikan dengan membandingkannya dengan Type Objects yang ditentukan pada bagian di bawah ini.

**.rowcount**

Atribut `read-only` ini menentukan jumlah baris yang dihasilkan `.execute*()` terakhir (untuk pernyataan `DQL like SELECT`) atau terpengaruh (untuk pernyataan `DML like UPDATE or INSERT`). Atributnya adalah -1 jika tidak ada `.execute*()` yang dilakukan pada kursor atau jumlah baris dari operasi terakhir tidak dapat ditentukan oleh antarmuka. 

`Catatan: Versi mendatang dari spesifikasi DB API dapat mendefinisikan kembali kasus terakhir agar objek kembali None, bukan -1.`

## Cursor methods

**.callproc ( procname [, parameter ] )**

(Metode ini opsional karena tidak semua database menyediakan prosedur tersimpan)

Panggil prosedur database tersimpan dengan nama yang diberikan. Urutan parameter harus berisi satu entri untuk setiap argumen yang diharapkan prosedur. Hasil panggilan dikembalikan sebagai salinan yang dimodifikasi dari urutan input. Parameter input dibiarkan tidak tersentuh, parameter output dan input/output diganti dengan nilai yang mungkin baru.

Prosedur juga dapat memberikan hasil yang ditetapkan sebagai output. Ini kemudian harus tersedia melalui metode `.fetch*()` standar.

**.close ()**

Tutup kursor sekarang (bukan kapan pun `__del__` dipanggil).

Kursor tidak akan dapat digunakan mulai saat ini; pengecualian Kesalahan (atau subkelas) akan dimunculkan jika ada operasi yang dicoba dengan kursor.

**.execute ( operasi [, parameter ])**

Mempersiapkan dan menjalankan operasi database (query atau perintah).
Parameter dapat diberikan sebagai urutan atau pemetaan dan akan terikat pada variabel dalam operasi. Variabel ditentukan dalam notasi khusus database (lihat atribut paramstyle modul untuk detailnya).

Referensi ke operasi akan disimpan oleh kursor. Jika objek operasi yang sama dilewatkan lagi, maka kursor dapat mengoptimalkan perilakunya. Ini paling efektif untuk algoritme di mana operasi yang sama digunakan, tetapi parameter yang berbeda terikat padanya (berkali-kali).

Untuk efisiensi maksimum saat menggunakan kembali operasi, yang terbaik adalah menggunakan metode `.setinputsizes()` untuk menentukan jenis dan ukuran parameter sebelumnya. Adalah sah jika suatu parameter tidak cocok dengan informasi yang telah ditentukan sebelumnya; implementasi harus mengimbangi, mungkin dengan hilangnya efisiensi.

Parameter juga dapat ditentukan sebagai daftar tupel untuk misalnya menyisipkan beberapa baris dalam satu operasi, tetapi penggunaan semacam ini tidak digunakan lagi: `.executemany()` harus digunakan sebagai gantinya.

Nilai kembalian tidak ditentukan.

**.executemany ( operasi , seq_of_parameters )**

Siapkan operasi database (query atau perintah) dan kemudian jalankan terhadap semua urutan parameter atau pemetaan yang ditemukan dalam urutan seq_of_parameters.
Modul bebas untuk mengimplementasikan metode ini menggunakan beberapa panggilan ke metode .execute() atau dengan menggunakan operasi array agar database memproses urutan secara keseluruhan dalam satu panggilan.

Penggunaan metode ini untuk operasi yang menghasilkan satu atau lebih kumpulan hasil merupakan perilaku yang tidak terdefinisi, dan implementasi diizinkan (tetapi tidak diperlukan) untuk memunculkan pengecualian ketika mendeteksi bahwa kumpulan hasil telah dibuat oleh pemanggilan operasi.

Komentar yang sama untuk `.execute()` juga berlaku untuk metode ini.

Nilai kembalian tidak ditentukan.

**.fetchone()**

Ambil baris berikutnya dari kumpulan hasil kueri, mengembalikan satu urutan, atau Nonesaat tidak ada lagi data yang tersedia.

Pengecualian Kesalahan (atau subkelas) muncul jika panggilan sebelumnya ke `.execute*()` tidak menghasilkan set hasil apa pun atau belum ada panggilan yang dikeluarkan.

**.fetchmany ([ size=kursor.arraysize ])**

Ambil set baris berikutnya dari hasil kueri, mengembalikan urutan urutan (misalnya daftar tupel). Urutan kosong dikembalikan ketika tidak ada lagi baris yang tersedia.

Jumlah baris yang akan diambil per panggilan ditentukan oleh parameter. Jika tidak diberikan, ukuran array kursor menentukan jumlah baris yang akan diambil. Metode ini harus mencoba mengambil baris sebanyak yang ditunjukkan oleh parameter ukuran. Jika ini tidak memungkinkan karena jumlah baris yang ditentukan tidak tersedia, lebih sedikit baris yang dapat dikembalikan.

Pengecualian Kesalahan (atau subkelas) muncul jika panggilan sebelumnya ke `.execute*()` tidak menghasilkan set hasil apa pun atau belum ada panggilan yang dikeluarkan.

Perhatikan ada pertimbangan kinerja yang terlibat dengan parameter ukuran. Untuk kinerja yang optimal, biasanya yang terbaik adalah menggunakan atribut `.arraysize`. Jika parameter size digunakan, maka yang terbaik adalah mempertahankan nilai yang sama dari satu panggilan `.fetchmany()` ke panggilan berikutnya.

**.fetchall()**

Ambil semua (sisa) baris hasil kueri, mengembalikannya sebagai urutan urutan (mis. daftar tupel). Perhatikan bahwa atribut arraysize kursor dapat mempengaruhi kinerja operasi ini.

Pengecualian Kesalahan (atau subkelas) muncul jika panggilan sebelumnya ke `.execute*()` tidak menghasilkan set hasil apa pun atau belum ada panggilan yang dikeluarkan.

**.nextset()**

(Metode ini opsional karena tidak semua database mendukung beberapa set hasil)
Metode ini akan membuat kursor melompat ke set berikutnya yang tersedia, membuang baris yang tersisa dari set saat ini.

Jika tidak ada set lagi, metode akan mengembalikan None. Jika tidak, ia mengembalikan nilai sebenarnya dan panggilan berikutnya ke metode `.fetch*()` akan mengembalikan baris dari kumpulan hasil berikutnya.

Pengecualian Kesalahan (atau subkelas) muncul jika panggilan sebelumnya ke `.execute*()` tidak menghasilkan set hasil apa pun atau belum ada panggilan yang dikeluarkan.

**.arraysize**

Atribut baca/tulis ini menentukan jumlah baris yang akan diambil sekaligus dengan `.fetchmany()`. Defaultnya adalah 1 yang berarti mengambil satu baris dalam satu waktu.

Implementasi harus mengamati nilai ini sehubungan dengan metode `.fetchmany()`, tetapi bebas untuk berinteraksi dengan database satu baris dalam satu waktu. Ini juga dapat digunakan dalam implementasi `.executemany()`.

**.setinputsizes(sizes)**

Ini dapat digunakan sebelum panggilan ke `.execute*()` untuk menentukan area memori untuk parameter operasi.

ukuran ditentukan sebagai urutan — satu item untuk setiap parameter input. Item harus berupa Objek Tipe yang sesuai dengan input yang akan digunakan, atau harus berupa bilangan bulat yang menentukan panjang maksimum parameter string. Jika itemnya adalah None, maka tidak ada area memori yang telah ditentukan sebelumnya yang akan dicadangkan untuk kolom tersebut (ini berguna untuk menghindari area yang telah ditentukan sebelumnya untuk input yang besar).

Metode ini akan digunakan sebelum metode `.execute*()` dipanggil.

Implementasi bebas agar metode ini tidak melakukan apa pun dan pengguna bebas untuk tidak menggunakannya.

**.setoutputsize(size [, column])**

Tetapkan ukuran penyangga kolom untuk pengambilan kolom besar (mis LONG. s, BLOBs, dll.). Kolom ditentukan sebagai indeks ke dalam urutan hasil. Tidak menentukan kolom akan menetapkan ukuran default untuk semua kolom besar di kursor.
Metode ini akan digunakan sebelum metode `.execute*()` dipanggil.

Implementasi bebas agar metode ini tidak melakukan apa pun dan pengguna bebas untuk tidak menggunakannya.

## Type Objects and Constructors

Banyak database perlu memiliki input dalam format tertentu untuk mengikat parameter input operasi. Misalnya, jika input ditujukan untuk DATEkolom, maka input tersebut harus diikat ke database dalam format string tertentu. Masalah serupa ada untuk kolom "ID Baris" atau item biner besar (mis. gumpalan atau RAW kolom). Ini menghadirkan masalah untuk Python karena parameter ke metode `.execute*()` tidak diketik. Ketika modul database melihat objek string Python, ia tidak tahu apakah itu harus diikat sebagai CHARkolom sederhana, sebagai `BINARY` item mentah, atau sebagai file `DATE`.

Untuk mengatasi masalah ini, sebuah modul harus menyediakan konstruktor yang didefinisikan di bawah ini untuk membuat objek yang dapat menyimpan nilai khusus. Ketika diteruskan ke metode kursor, modul kemudian dapat mendeteksi tipe yang tepat dari parameter input dan mengikatnya.

Atribut deskripsi Objek Kursor mengembalikan informasi tentang masing-masing kolom hasil kueri. type_codeHarus membandingkan sama dengan salah satu Objek Jenis didefinisikan di bawah ini . Jenis Objek mungkin sama dengan lebih dari satu kode jenis (misalnya `DATETIME` bisa sama dengan kode jenis untuk kolom tanggal, waktu dan stempel waktu; lihat Petunjuk Implementasi di bawah untuk detailnya).

Modul mengekspor konstruktor dan lajang berikut:

Date(year, month, day)
 - Fungsi ini membangun sebuah objek yang memegang nilai tanggal.

Time(hour, minute, second)
 - Fungsi ini membangun objek yang memiliki nilai waktu.

Timestamp(year, month, day, hour, minute, second)
 - Fungsi ini membangun sebuah objek yang memegang nilai cap waktu.

DateFromTicks(ticks)
 - Fungsi ini membuat objek yang menyimpan nilai tanggal dari nilai tick yang diberikan (jumlah detik sejak Epoch; lihat dokumentasi modul waktu Python standar untuk detailnya).

TimeFromTicks(ticks)
 - Fungsi ini membangun objek yang memegang nilai waktu dari nilai tick yang diberikan (jumlah detik sejak Epoch; lihat dokumentasi modul waktu Python standar untuk detailnya).

TimestampFromTicks(ticks)
 - Fungsi ini membuat objek yang menyimpan nilai cap waktu dari nilai tick yang diberikan (jumlah detik sejak epoch; lihat dokumentasi modul waktu Python standar untuk detailnya).

Binary(string)
 - Fungsi ini membangun objek yang mampu menyimpan nilai string biner (panjang).

STRING type
 - Objek tipe ini digunakan untuk mendeskripsikan kolom dalam database yang berbasis string (mis CHAR.).

BINARY type
 - Jenis objek ini digunakan untuk menggambarkan (panjang) kolom biner dalam database (misalnya LONG, RAW, BLOBs).

NUMBER type
 - Objek tipe ini digunakan untuk menggambarkan kolom numerik dalam database.

DATETIME type
 - Objek tipe ini digunakan untuk mendeskripsikan kolom tanggal/waktu dalam database.

ROWID type
 - Objek tipe ini digunakan untuk mendeskripsikan kolom “Row ID” dalam database.

Nilai SQL NULL diwakili oleh Nonesingleton Python pada input dan output.

`Catatan: Penggunaan kutu Unix untuk antarmuka basis data dapat menyebabkan masalah karena rentang tanggal terbatas yang dicakupnya.`

---


# PSYCOPG

`Psycopg` adalah adaptor PostgreSQL paling populer untuk bahasa pemrograman Python. Intinya adalah implementasi lengkap dari spesifikasi Python DB API 2.0. Beberapa ekstensi memungkinkan akses ke banyak fitur yang ditawarkan oleh PostgreSQL.

Salah satu tujuan proyek `Psycopg 3` adalah untuk memudahkan kode port yang dikembangkan dari `Psycopg 2`. Untuk alasan ini pembuatan backend Django (modul yang Anda tentukan dalam pengaturan sebagai database ENGINE Kita) adalah proyek dengan tujuan ganda :
 * Driver Django adalah cara untuk membuat Psycopg 3 berguna sejak awal, dengan kemungkinan menjatuhkannya dalam proyek secara transparan dan telah tersedia, bila diperlukan fitur baru yang ditawarkan (misalnya dukungan COPY superior ).
 * Kesulitan dalam memperkenalkan Psycopg 3 dalam basis kode Django dan jenis perubahan yang diperlukan adalah indikasi dari jenis masalah yang dapat ditemukan pada port proyek lain.

---

# PyMongo

Distribusi `PyMongo` berisi alat untuk berinteraksi dengan database MongoDB dari Python. Paket `bsonini` merupakan implementasi dari format BSON untuk Python. Paket pymongo ini adalah driver Python asli untuk MongoDB. Paket `gridfsini` adalah implementasi gridfs di atas pymongo.

PyMongo mendukung MongoDB 3.6, 4.0, 4.2, 4.4, dan 5.0.

## Dukungan / Umpan Balik

Untuk masalah, pertanyaan tentang, atau umpan balik untuk PyMongo, silakan lihat saluran dukungan kami . Harap jangan mengirim email kepada pengembang PyMongo secara langsung dengan masalah atau pertanyaan - Anda kemungkinan besar akan mendapatkan jawaban di Forum Komunitas MongoDB.

## Bug / Permintaan Fitur

Pikirkan Anda telah menemukan bug? Ingin melihat fitur baru di PyMongo? Silakan buka kasus di alat manajemen masalah kami, JIRA:

 * Buat akun dan login.
 * Navigasikan ke proyek PYTHON.
 * Klik Buat Masalah - Berikan informasi sebanyak mungkin tentang jenis masalah dan cara mereproduksinya.
 * Laporan bug di JIRA untuk semua proyek driver (yaitu PYTHON, CSHARP, JAVA) dan proyek Core Server (yaitu SERVER)  * bersifat publik.

**Cara Meminta Bantuan**

Harap sertakan semua informasi berikut saat membuka masalah:

Langkah-langkah mendetail untuk mereproduksi masalah, termasuk penelusuran balik penuh, jika memungkinkan.

* Versi python persis yang digunakan, dengan level tambalan:

```python
$ python -c "impor sys; print(sys.version)"
```

* Versi persis PyMongo yang digunakan, dengan level tambalan:

```python
$ python -c "impor pymongo; print(pymongo.version); print(pymongo.has_c())"
```

* Sistem operasi dan versi (misalnya Windows 7, OSX 10.8, ...)

* Kerangka kerja web atau pustaka jaringan asinkron yang digunakan, jika ada, dengan versi (misalnya Django 1.7, mod_wsgi 4.3.0, gevent 1.0.1, Tornado 4.0.2, ...)

**Kerentanan Keamanan**

Jika Anda telah mengidentifikasi kerentanan keamanan pada driver atau proyek MongoDB lainnya, harap laporkan sesuai dengan petunjuk di sini.

## Instalasi

PyMongo dapat diinstal dengan pip :

```python
$ python -m pip instal pymongo
```

Atau `easy_install` dari setuptools :

```python
$ python -m easy_install pymongo
```
Anda juga dapat mengunduh sumber proyek dan melakukan:

```python
$ python setup.py install
```

Jangan instal paket " bson" dari pypi. PyMongo hadir dengan paket bsonnya sendiri; melakukan `"easy_install bson"` menginstal paket pihak ketiga yang tidak kompatibel dengan PyMongo.

## Dependencies

PyMongo mendukung CPython 3.7+ dan PyPy3.7+.

Dependensi opsional:

Otentikasi GSSAPI memerlukan pykerberos di Unix atau WinKerberos di Windows. Ketergantungan yang benar dapat diinstal secara otomatis bersama dengan PyMongo:


```python
$ python -m pip instal "pymongo[gssapi]"
```
Otentikasi MONGODB-AWS memerlukan pymongo-auth-aws :

```python
$ python -m pip instal "pymongo[aws]"
```

Dukungan untuk mongodb+srv:// URI membutuhkan dnspython :

```python
$ python -m pip instal "pymongo[srv]"
```

OCSP (Protokol Status Sertifikat Online) memerlukan PyOpenSSL , request , service_identity dan mungkin memerlukan certifi :

```python
$ python -m pip instal "pymongo[ocsp]"
```

Kompresi protokol kawat dengan snappy membutuhkan python-snappy :

```python
$ python -m pip instal "pymongo[snappy]"
```

Kompresi protokol kawat dengan zstandard membutuhkan zstandard :

```python
$ python -m pip instal "pymongo[zstd]"
```

Enkripsi Tingkat Bidang Sisi Klien memerlukan pymongocrypt :

```python
$ python -m pip instal "pymongo[enkripsi]"
```

Anda dapat menginstal semua dependensi secara otomatis dengan perintah berikut:

```python
$ python -m pip install "pymongo[gssapi,aws,ocsp,snappy,srv,tls,zstd,encryption]"
```

Dependensi tambahan adalah:

 * (untuk menghasilkan dokumentasi) sphinx

Contoh

Berikut adalah contoh dasar (untuk lebih lanjut lihat bagian contoh dari dokumen):

```python
>> >  impor  pymongo 
>> >  client  =  pymongo . MongoClient ( "localhost" , 27017 )
 >> >  db  =  klien . tes 
>> >  db . nama 
'tes' 
>> >  db . Koleksi my_collection
 ( Database ( MongoClient ( 'localhost' , 27017 ), 'test' ), 'my_collection' db . koleksi_saya . insert_one ({ "x" : 10 }). insert_id ObjectId (
 ' 4aba15ebe23f6b53b0000000' )
 >> > db . koleksi_saya . insert_one ({ "x" : 8 }). insert_id ObjectId ( ' 4aba160ee23f6b543e000000' )
 >> > db . koleksi_saya . insert_one ({ "x" : 11 }). insert_id ObjectId ( 
 
'4aba160ee23f6b543e000002' )
 >> >  db . koleksi_saya . temukan_satu ()
{ 'x' : 10 , '_id' : ObjectId ( '4aba15ebe23f6b53b0000000' )}
 >> >  untuk  item  dalam  db . koleksi_saya . temukan ():
...      print ( item [ "x" ])
...
10 
8 
11 
>> >  db . koleksi_saya . create_index ( "x" )
 'x_1' 
>> >  untuk  item  dalam  db . koleksi_saya . temukan (). sort ( "x" , pymongo . ASCENDING ):
...      print ( item [ "x" ])
...
8 
10 
11 
>> > [ item [ "x" ] untuk  item  dalam  db . koleksi_saya . temukan (). batas ( 2 ). lewati ( 1 )]
[ 8 , 11 ]
```

## Dokumentasi

Dokumentasi tersedia di `pymongo.readthedocs.io`.

Untuk membuat dokumentasi, Anda perlu menginstal sphinx . Dokumentasi dapat dibuat dengan menjalankan python setup.py doc . Dokumentasi yang dihasilkan dapat ditemukan di direktori doc/build/html/ .

## Pengujian

Cara termudah untuk menjalankan tes adalah dengan menjalankan python setup.py test di root distribusi.

Untuk memverifikasi bahwa PyMongo berfungsi dengan penambalan monyet Gevent:

```python
$ python green_framework_test.py gevent
```
Atau dengan Eventlet's:

```python
$ python green_framework_test.py eventlet
```

---

# SQLAlchemy

**Python SQL Toolkit dan Object Relational Mapper**

`SQLAlchemy` adalah toolkit Python SQL dan Object Relational Mapper yang memberi pengembang aplikasi kekuatan penuh dan fleksibilitas SQL.

Ini menyediakan rangkaian lengkap pola persistensi tingkat perusahaan yang terkenal, dirancang untuk akses database yang efisien dan berkinerja tinggi, diadaptasi ke dalam bahasa domain yang sederhana dan Pythonic.

**FILOSOFI SQLALCHEMY**

Basis data SQL berperilaku kurang seperti koleksi objek, semakin banyak ukuran dan kinerja mulai menjadi masalah; koleksi objek berperilaku kurang seperti tabel dan baris semakin abstraksi mulai penting. SQLAlchemy bertujuan untuk mengakomodasi kedua prinsip ini.

SQLAlchemy menganggap database sebagai mesin aljabar relasional, bukan hanya kumpulan tabel. Baris dapat dipilih tidak hanya dari tabel tetapi juga gabungan dan pernyataan pemilihan lainnya; salah satu dari unit ini dapat disusun menjadi struktur yang lebih besar. Bahasa ekspresi SQLAlchemy dibangun di atas konsep ini dari intinya.

SQLAlchemy paling terkenal dengan object-relational mapper (ORM), komponen opsional yang menyediakan pola data mapper, di mana kelas dapat dipetakan ke database secara terbuka, dengan berbagai cara - memungkinkan model objek dan skema database untuk berkembang dalam dipisahkan dengan cara yang bersih dari awal.

Pendekatan keseluruhan SQLAlchemy untuk masalah ini sama sekali berbeda dari kebanyakan alat SQL / ORM lainnya, berakar pada apa yang disebut pendekatan berorientasi pujian; alih-alih menyembunyikan SQL dan detail relasional objek di balik dinding otomatisasi, semua proses diekspos sepenuhnya dalam serangkaian alat yang dapat disusun dan transparan. Pustaka mengambil tugas mengotomatisasi tugas-tugas yang berlebihan sementara pengembang tetap mengendalikan bagaimana database diatur dan bagaimana SQL dibangun.

Tujuan utama SQLAlchemy adalah mengubah cara berpikir Anda tentang database dan SQL!

SQLAlchemy is used by organizations such as:
 * Yelp!
 * reddit
 * DropBox
 * The OpenStack Project
 * Survey Monkey

---

# Build a Python App with CockroachDB and psycopg2

## Use CockroachDB Serverless (beta)

1. Jika Anda belum melakukannya, daftar akun CockroachDB Cloud.

2. Masuk ke akun Cloud CockroachDB Anda.

3. Pada halaman Cluster , klik Buat Cluster.

4. Pada halaman Buat kluster Anda , pilih Tanpa Server.

Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.

5. Klik Buat kluster.

Cluster Anda akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

**Buat pengguna SQL**

Dialog Buat pengguna SQL memungkinkan Anda membuat pengguna dan kata sandi SQL baru.

1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.

3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.

4. Klik Berikutnya.

**Dapatkan sertifikat root**

Dialog Hubungkan ke klaster menampilkan informasi tentang cara menghubungkan ke klaster Anda.

1. Pilih String koneksi umum dari dropdown Pilih opsi .

2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

**Dapatkan string koneksi**

Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

`Catatan: String koneksi sudah diisi sebelumnya dengan nama pengguna, kata sandi, nama cluster, dan detail lainnya. Kata sandi Anda, khususnya, hanya akan diberikan sekali . Simpan di tempat yang aman (Cockroach Labs merekomendasikan pengelola kata sandi) untuk terhubung ke cluster Anda di masa mendatang. Jika Anda lupa kata sandi, Anda dapat mengatur ulang dengan membuka halaman Pengguna SQL .`

**Langkah 2. Dapatkan kode sampel**

Kloning repo GitHub kode sampel:

```python
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```
Kode sampel di example.pymelakukan hal berikut:

 * Membuat accounts tabel dan menyisipkan beberapa baris
 * Mentransfer dana antara dua akun dalam suatu transaksi
 * Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali kode contoh

Untuk menangani kesalahan percobaan ulang transaksi , kode menggunakan pengulangan percobaan tingkat aplikasi yang, jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan backoff eksponensial.

**Langkah 3. Instal driver psycopg2**

psycopg2-binary adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal psycopg2-binary, jalankan perintah berikut:

```python
$ pip install psycopg2-binary
```

**Langkah 4. Jalankan kode**

1. Setel DATABASE_URL variabel lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda:

```python
$ export DATABASE_URL="{connection-string}"
```

Di mana {connection-string}string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan kode:

```python
$ cd hello-world-python-psycopg2
```

```python
$ python example.py
```

Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:

```python
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```

## Use a Local Cluster

1. Jika Anda belum melakukannya, unduh biner CockroachDB.

2. Jalankan cockroach start-single-nodeperintah:

```python
$ cockroach start-single-node --advertise-addr 'localhost' --insecure
```

Ini memulai cluster node tunggal yang tidak aman.

```python
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
```

**Langkah 2. Dapatkan kode sampel**

Kloning repo GitHub kode sampel:

```python
$ git clone https://github.com/cockroachlabs/hello-world-python-psycopg2
```

Kode sampel di example.pymelakukan hal berikut:

 * Membuat accountstabel dan menyisipkan beberapa baris
 * Mentransfer dana antara dua akun dalam suatu transaksi
 * Hapus akun dari tabel sebelum keluar sehingga Anda dapat menjalankan kembali kode contoh

Untuk menangani kesalahan percobaan ulang transaksi , kode menggunakan pengulangan percobaan tingkat aplikasi yang, jika terjadi kesalahan, tidur sebelum mencoba transfer dana lagi. Jika menemukan kesalahan coba lagi, ia tidur untuk interval yang lebih lama, menerapkan backoff eksponensial.

**Langkah 3. Instal driver psycopg2**

psycopg2-binary adalah satu-satunya dependensi modul pihak ketiga aplikasi sampel.

Untuk menginstal psycopg2-binary, jalankan perintah berikut:

```python
$ pip install psycopg2-binary
```

**Langkah 4. Jalankan kode**

1. Setel DATABASE_URL variabel lingkungan ke string koneksi ke cluster CockroachDB Cloud Anda:

```python
$ export DATABASE_URL="postgresql://root@localhost:26257?sslmode=disable"
```

Aplikasi menggunakan string koneksi yang disimpan ke DATABASE_URL variabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan kode:

```python
$ cd hello-world-python-psycopg2
```

```python
$ python example.py
```
Output harus menunjukkan saldo akun sebelum dan sesudah transfer dana:

```python
Balances at Fri Oct 30 18:27:00 2020:
(1, 1000)
(2, 250)
Balances at Fri Oct 30 18:27:00 2020:
(1, 900)
(2, 350)
```

---

# Build a Simple CRUD Python App with CockroachDB and SQLAlchemy

**Langkah 1. Mulai CockroachDB**

***Gunakan CockroachDB Tanpa Server (beta)***

Buat cluster gratis

1. Jika Anda belum melakukannya, daftar akun CockroachDB Cloud.
2. Masuk ke akun Cloud CockroachDB Anda.
3. Pada halaman Cluster , klik Buat Cluster.
4. Pada halaman Buat kluster Anda , pilih Tanpa Server.

Kecuali Anda mengubah anggaran bulanan, cluster ini akan gratis selamanya.

5. Klik Buat kluster.

Cluster Anda akan dibuat dalam beberapa detik dan dialog Buat pengguna SQL akan ditampilkan.

Buat pengguna SQL

Dialog Buat pengguna SQL memungkinkan Anda membuat pengguna dan kata sandi SQL baru.

1. Masukkan nama pengguna di bidang pengguna SQL atau gunakan yang disediakan secara default.
2. Klik Buat & simpan kata sandi.
3. Salin kata sandi yang dihasilkan dan simpan di lokasi yang aman.
4. Klik Berikutnya.

Dapatkan sertifikat root

Dialog Hubungkan ke klaster menampilkan informasi tentang cara menghubungkan ke klaster Anda.

1. Pilih String koneksi umum dari dropdown Pilih opsi .
2. Buka terminal baru di komputer lokal Anda, dan jalankan perintah unduhan CA Cert yang disediakan di bagian Unduh CA Cert . Driver klien yang digunakan dalam tutorial ini memerlukan sertifikat ini untuk terhubung ke CockroachDB Cloud.

Dapatkan string koneksi

Buka bagian General connection string , lalu salin connection string yang disediakan dan simpan di lokasi yang aman.

`Catatan: String koneksi sudah diisi sebelumnya dengan nama pengguna, kata sandi, nama cluster, dan detail lainnya. Kata sandi Anda, khususnya, hanya akan diberikan sekali . Simpan di tempat yang aman (Cockroach Labs merekomendasikan pengelola kata sandi) untuk terhubung ke cluster Anda di masa mendatang. Jika Anda lupa kata sandi, Anda dapat mengatur ulang dengan membuka halaman Pengguna SQL.`

**Langkah 2. Dapatkan kodenya**

Kloning kode repo GitHub:

```python
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```
Proyek ini memiliki struktur direktori berikut:

```python
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```

File requirements.txt tersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdb paket Python , yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL:

```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```

File dbinit.sql menginisialisasi skema database yang digunakan aplikasi:

```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```

Menggunakan SQLAlchemy models.py untuk memetakan Accounts tabel ke objek Python:

```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```

Menggunakan SQLAlchemy main.py untuk memetakan metode Python ke operasi SQL:

```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```

main.py juga mengeksekusi mainmetode program.

**Langkah 3. Instal persyaratan aplikasi**

Tutorial ini digunakan virtualenvuntuk manajemen ketergantungan.

Instal virtualenv:

```python
$ pip install virtualenv
```

Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual:

```python
$ virtualenv env
$ source env/bin/activate
```

Instal modul yang diperlukan ke lingkungan virtual:

```python
$ pip install -r requirements.txt
```

**Langkah 4. Inisialisasi database**

Setel DATABASE_URL variabel lingkungan ke string koneksi untuk cluster Anda:

```python
export DATABASE_URL="{connection-string}"
```

Di mana {connection-string} string koneksi yang Anda peroleh dari CockroachDB Cloud Console.

Untuk menginisialisasi database contoh, gunakan cockroach sqlperintah untuk mengeksekusi pernyataan SQL dalam dbinit.sqlfile:

```python
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```

Pernyataan SQL dalam file inisialisasi harus dijalankan:

```sql
CREATE TABLE

Time: 102ms
```

**Langkah 5. Jalankan kodenya**

main.py menggunakan string koneksi yang disimpan ke DATABASE_URL variabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan aplikasi:

```python
python main.py
```

Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut:

```python
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```

Dalam shell SQL yang terhubung ke cluster, Anda dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus:

```sql
SELECT COUNT(*) FROM accounts;
  count
---------
     95
(1 row)
```

---

***Gunakan Cluster Lokal***

1. Jika Anda belum melakukannya, unduh biner CockroachDB.

2. Jalankan cockroach start-single-nodeperintah:

```python
$ cockroach start-single-node --advertise-addr 'localhost' --insecure
```

Ini memulai cluster node tunggal yang tidak aman.

```python
CockroachDB node starting at 2021-08-30 17:25:30.06524 +0000 UTC (took 4.3s)
build:               CCL v21.1.6 @ 2021/07/20 15:33:43 (go1.15.11)
webui:               http://localhost:8080
sql:                 postgresql://root@localhost:26257?sslmode=disable
```

**Langkah 2. Dapatkan kodenya**

Kloning kode repo GitHub:

```python
$ git clone https://github.com/cockroachlabs/example-app-python-sqlalchemy/
```

Proyek ini memiliki struktur direktori berikut:

```python
├── README.md
├── dbinit.sql
├── main.py
├── models.py
└── requirements.txt
```
File requirements.txt tersebut menyertakan pustaka yang diperlukan untuk terhubung ke CockroachDB dengan SQLAlchemy, termasuk sqlalchemy-cockroachdb paket Python , yang menjelaskan beberapa perbedaan antara CockroachDB dan PostgreSQL:

```python
psycopg2-binary
sqlalchemy
sqlalchemy-cockroachdb
```

File dbinit.sql menginisialisasi skema database yang digunakan aplikasi:

```sql
CREATE TABLE accounts (
    id UUID PRIMARY KEY,
    balance INT8
);
```

Menggunakan SQLAlchemy models.py untuk memetakan Accountstabel ke objek Python:

```python
from sqlalchemy import Column, Integer
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Account(Base):
    """The Account class corresponds to the "accounts" database table.
    """
    __tablename__ = 'accounts'
    id = Column(UUID(as_uuid=True), primary_key=True)
    balance = Column(Integer)
```
Menggunakan SQLAlchemy main.py untuk memetakan metode Python ke operasi SQL:

```python
"""This simple CRUD application performs the following operations sequentially:
    1. Creates 100 new accounts with randomly generated IDs and randomly-computed balance amounts.
    2. Chooses two accounts at random and takes half of the money from the first and deposits it
     into the second.
    3. Chooses five accounts at random and deletes them.
"""

from math import floor
import os
import random
import uuid

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy_cockroachdb import run_transaction
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from models import Account

# The code below inserts new accounts.


def create_accounts(session, num):
    """Create N new accounts with random account IDs and account balances.
    """
    print("Creating new accounts...")
    new_accounts = []
    while num > 0:
        account_id = uuid.uuid4()
        account_balance = floor(random.random()*1_000_000)
        new_accounts.append(Account(id=account_id, balance=account_balance))
        seen_account_ids.append(account_id)
        print(f"Created new account with id {account_id} and balance {account_balance}.")
        num = num - 1
    session.add_all(new_accounts)


def transfer_funds_randomly(session, one, two):
    """Transfer money between two accounts.
    """
    try:
        source = session.query(Account).filter(Account.id == one).one()
    except NoResultFound:
        print("No result was found")
    except MultipleResultsFound:
        print("Multiple results were found")
    dest = session.query(Account).filter(Account.id == two).first()
    print(f"Random account balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")

    amount = floor(source.balance/2)
    print(f"Transferring {amount} from account {one} to account {two}...")

    # Check balance of the first account.
    if source.balance < amount:
        raise ValueError(f"Insufficient funds in account {one}")
    source.balance -= amount
    dest.balance += amount

    print(f"Transfer complete.\nNew balances:\nAccount {one}: {source.balance}\nAccount {two}: {dest.balance}")


def delete_accounts(session, num):
    """Delete N existing accounts, at random.
    """
    print("Deleting existing accounts...")
    delete_ids = []
    while num > 0:
        delete_id = random.choice(seen_account_ids)
        delete_ids.append(delete_id)
        seen_account_ids.remove(delete_id)
        num = num - 1

    accounts = session.query(Account).filter(Account.id.in_(delete_ids)).all()

    for account in accounts:
        print(f"Deleted account {account.id}.")
        session.delete(account)


if __name__ == '__main__':
    # For cockroach demo:
    # DATABASE_URL=postgresql://demo:<demo_password>@127.0.0.1:26257?sslmode=require
    # For CockroachCloud:
    # DATABASE_URL=postgresql://<username>:<password>@<globalhost>:26257/<cluster_name>.defaultdb?sslmode=verify-full&sslrootcert=<certs_dir>/<ca.crt>
    db_uri = os.environ['DATABASE_URL'].replace("postgresql://", "cockroachdb://")
    try:
        engine = create_engine(db_uri)
    except Exception as e:
        print("Failed to connect to database.")
        print(f"{e}")

    seen_account_ids = []

    run_transaction(sessionmaker(bind=engine),
                    lambda s: create_accounts(s, 100))

    from_id = random.choice(seen_account_ids)
    to_id = random.choice([id for id in seen_account_ids if id != from_id])

    run_transaction(sessionmaker(bind=engine),
                    lambda s: transfer_funds_randomly(s, from_id, to_id))

    run_transaction(sessionmaker(bind=engine), lambda s: delete_accounts(s, 5))
```

main.py juga mengeksekusi mainmetode program.

**Langkah 3. Instal persyaratan aplikasi**

Tutorial ini digunakan virtualenvuntuk manajemen ketergantungan.

Instal virtualenv:

```python
pip install virtualenv
```

Di tingkat atas direktori proyek aplikasi, buat lalu aktifkan lingkungan virtual:

```python
virtualenv env
source env/bin/activate
```

Instal modul yang diperlukan ke lingkungan virtual:

```python
pip install -r requirements.txt
```

**Langkah 4. Inisialisasi database**

Setel DATABASE_URL variabel lingkungan ke string koneksi untuk cluster Anda:

```python
export DATABASE_URL="postgresql://root@localhost:26257?sslmode=disable"
```

Untuk menginisialisasi database contoh, gunakan cockroach sqlperintah untuk mengeksekusi pernyataan SQL dalam dbinit.sqlfile:

```python
cat dbinit.sql | cockroach sql --url $DATABASE_URL
```

Pernyataan SQL dalam file inisialisasi harus dijalankan:

```sql
CREATE TABLE

Time: 102ms
```

**Langkah 5. Jalankan kodenya**

main.py menggunakan string koneksi yang disimpan ke DATABASE_URLvariabel lingkungan untuk terhubung ke cluster Anda dan mengeksekusi kode.

Jalankan aplikasi:

```python
python main.py
```

Aplikasi akan terhubung ke CockroachDB, dan kemudian melakukan beberapa penyisipan baris sederhana, pembaruan, dan penghapusan.

Outputnya akan terlihat seperti berikut:

```python
Creating new accounts...
Created new account with id 3a8b74c8-6a05-4247-9c60-24b46e3a88fd and balance 248835.
Created new account with id c3985926-5b77-4c6d-a73d-7c0d4b2a51e7 and balance 781972.
...
Created new account with id 7b41386c-11d3-465e-a2a0-56e0dcd2e7db and balance 984387.
Random account balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 800795
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 149861
Transferring 400397 from account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9 to account 4040aeba-7194-4f29-b8e5-a27ed4c7a297...
Transfer complete.
New balances:
Account 7ad14d02-217f-48ca-a53c-2c3a2528a0d9: 400398
Account 4040aeba-7194-4f29-b8e5-a27ed4c7a297: 550258
Deleting existing accounts...
Deleted account 41247e24-6210-4032-b622-c10b3c7222de.
Deleted account 502450e4-6daa-4ced-869c-4dff62dc52de.
Deleted account 6ff06ef0-423a-4b08-8b87-48af2221bc18.
Deleted account a1acb134-950c-4882-9ac7-6d6fbdaaaee1.
Deleted account e4f33c55-7230-4080-b5ac-5dde8a7ae41d.
```

Dalam shell SQL yang terhubung ke cluster, Anda dapat memverifikasi bahwa baris berhasil dimasukkan, diperbarui, dan dihapus:

```sql
SELECT COUNT(*) FROM accounts;
  count
---------
     95
(1 row)
```
