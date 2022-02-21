# BAB 4 Control Flow

Selain pernyataan while yang telah dibahas pada bab sebelumnya, Python juga menggunakan pernyataan kontrol aliran (control flow) yang juga dikenal di bahasa lainnya, dengan beberapa kesamaan. Control Flow adalah urutan di mana pernyataan individu, instruksi atau panggilan fungsi dari program penting dijalankan atau dievaluasi. Penekanan pada aliran kontrol eksplisit membedakan bahasa pemrograman imperatif dari bahasa pemrograman deklaratif.

**Pernyataan IF**

Pada python ada beberapa statement/kondisi diantaranya adalah if, else, dan elif. Kondisi if digunakan untuk mengeksekusi kode jika kondisi bernilai benar True . Jika kondisi bernilai salah False maka statement/kondisi if tidak akan di-eksekusi. Sebagai contoh:

```python
>>> x = int(input("Please enter an integer: "))
Please enter an integer: 42
>>> if x < 0:
...     x = 0
...     print('Negative changed to zero')
... elif x == 0:
...     print('Zero')
... elif x == 1:
...     print('Single')
... else:
...     print('More')
...
More #output
```

Untuk elif adalah kependekan dari `else if` yang berguna untuk menghindari indentasi yang berlebihan. Di dalam python, indentasi (tulisan sedikit menjorok ke kanan) sangatlah mempengaruhi hasil eksekusi. untuk mengeksekusi kode script, maka klik icon segitiga hijau besar (untuk eksekusi seluruhnya), atau segitiga hijau dengan garis (untuk eksekusi beberapa line yang Anda blok). Sebuah urutan `if ... elif ... elif ...` adalah urutan persamaan dari pernyataan `switch` dan `case`.

**Pernyataan FOR**

Seperti di bahasa pemrograman lainnya, Python juga memiliki fungsi for. Bedanya di Python, For tidak hanya untuk perulangan dengan jumlah finite (terbatas), melainkan lebih ke fungsi yang dapat melakukan perulangan pada setiap jenis variabel berupa kumpulan atau urutan.

Pernyataan for dalam Python sedikit berbeda dari apa yang mungkin kita gunakan di C atau Pascal. Pada python, pernyataan for diulangi pada item-item dari urutan apa pun (daftar list atau string), dalam urutan yang muncul dalam urutan. Contoh:

```python
>>> # Mengukur beberapa string:
... words = ['cat', 'window', 'defenestrate']
>>> for w in words:
...     print(w, len(w))
...
# Output
cat 3
window 6
defenestrate 12
```

Kemudian berikut ini penggunaan perulangan for dalam pembuatan collection pada Python:

```python
# Membuat sebuah koleksi sampel
users = {'Hans': 'active', 'Éléonore': 'inactive', '景太郎': 'active'}

# Strategi: Ulangi salinan
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategi: Buat koleksi baru
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status
```

**Fungsi range()**

range() adalah sebuah fungsi serbaguna yang gunanya untuk menciptakan sebuah list yang terdiri dari angka. Instruksi: Parameter di range() bisa terdiri dari satu hingga tiga parameter. urutan yang dihasilkan merupakan urutan pregressions aritmatika contohnya seperti:

```python
>>> for i in range(5):
...     print(i)
...
0
1
2
3
4
```
Dalam penggunaan fungsi range() dapat digabungkan dengan fungsi list() untuk membuat sebuah urutan dan nilai dapat ditentukan sesuai yang diinginkan. Contohnya:

```python
>>> list(range(5, 10))
[5, 6, 7, 8, 9]

>>> list(range(0, 10, 3))
[0, 3, 6, 9]

>>> list(range(-10, -100, -30))
[-10, -40, -70]
```

Kemudian penggabungan dari fungsi range() dan len() dengan contohnya:

```python
>>> a = ['Mary', 'had', 'a', 'little', 'lamb']
>>> for i in range(len(a)):
...     print(i, a[i])
...
0 Mary
1 had
2 a
3 little
4 lamb
```

Dalam kasus seperti di atas, untuk memudahkannya dapat menggunakan konsep dari funsi enumerate(). Fungsi enumerate() mengembalikan nilai berupa objek enumerate. Objek enumerate sendiri merupakan objek iterable yang tiap itemnya berpasangan dengan indeks atau angka yang mewakilinya. Dengan kata lain fungsi ini akan menambahkan penghitung (indeks) ke objek iterable dan mengembalikannya. Pada implementasi range() juga dapat digabungkan dengan fungsi sum() contohnya:

```python
>>> sum(range(4))  # 0 + 1 + 2 + 3
6
```

**4.4. Pernyataan break dan continue, dan else Klausa pada Perulangan Loops**

Pertanyaan break, seperti dalam C, pada python juga digunakan dalam perulangan for atau while. Dengan kata lain, break adalah perintah khusus yang dipakai untuk memaksa sebuah perulangan berhenti sebelum waktunya. Sebagai contohnya pada program mencari bilangan prima:

```python
>>> for n in range(2, 10):
...     for x in range(2, n):
...         if n % x == 0:
...             print(n, 'equals', x, '*', n//x)
...             break
...     else:
...         # loop fell through without finding a factor
...         print(n, 'is a prime number')
...
2 is a prime number
3 is a prime number
4 equals 2 * 2
5 is a prime number
6 equals 2 * 3
7 is a prime number
8 equals 2 * 4
9 equals 3 * 3
```

Kemudian pernyataan continue yang berfungsi untuk lompat ke iterasi selanjutnya tanpa harus mengeksekusi sisa kode yang ada di bawahnya. Contohnya:

```python
>>> for num in range(2, 10):
...     if num % 2 == 0:
...         print("Found an even number", num)
...         continue
...     print("Found an odd number", num)
...
Found an even number 2
Found an odd number 3
Found an even number 4
Found an odd number 5
Found an even number 6
Found an odd number 7
Found an even number 8
Found an odd number 9
```

**4.5. Pernyataan Pass**

Kata kunci pass adalah sebuah statemen pada python yang tidak memiliki tugas apa pun. Tidak menginstruksi sistem untuk melakukan satu hal pun. Pernyataan pass tidak melakukan apa-apa. Ini dapat digunakan ketika pernyataan diperlukan secara sintaksis tetapi program tidak memerlukan tindakan. Sebagai contoh:

```python
>>> while True:
...     pass  # Busy-wait for keyboard interrupt (Ctrl+C)
...
```

atau

```python
>>> class MyEmptyClass:
...     pass
...
```

pass juga dapat digunakan adalah sebagai tempat-penampung place-holder untuk fungsi atau badan bersyarat conditional body saat Anda bekerja pada kode baru, memungkinkan Anda untuk terus berpikir pada tingkat yang lebih abstrak. Contohnya:

```python
>>> def initlog(*args):
...     pass   # Remember to implement this!
...
```

**4.6. Pernyataan Match**

Pernyataan match mengambil ekspresi dan membandingkan nilainya dengan pola berurutan yang diberikan sebagai satu atau lebih blok kasus. pernyataan ini mirip dengan pernyataan Switch di C, Java atau JavaScript (dan banyak bahasa lainnya), tetapi juga dapat mengekstrak komponen (elemen urutan atau atribut objek) dari nilai ke dalam variabel. Contohnya:

```python
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"
```

Kita dapat menggabungkan beberapa literal dalam satu pola menggunakan `|` atau operator `or`

```python
case 401 | 403 | 404:
    return "Not allowed"
```

```python
# point is an (x, y) tuple
match point:
    case (0, 0):
        print("Origin")
    case (0, y):
        print(f"Y={y}")
    case (x, 0):
        print(f"X={x}")
    case (x, y):
        print(f"X={x}, Y={y}")
    case _:
        raise ValueError("Not a point")
```

Jika kita menggunakan kelas, kita dapat menggunakan nama kelas diikuti dengan daftar argumen yang menyerupai konstruktor, tetapi dengan kemampuan untuk menangkap atribut ke dalam variabel:

```python
class Point:
    x: int
    y: int

def where_is(point):
    match point:
        case Point(x=0, y=0):
            print("Origin")
        case Point(x=0, y=y):
            print(f"Y={y}")
        case Point(x=x, y=0):
            print(f"X={x}")
        case Point():
            print("Somewhere else")
        case _:
            print("Not a point")
```

Pola pada python dapat bersarang secara sewenang-wenang. Misalnya, jika kita memiliki daftar poin pendek, kita bisa mencocokkannya seperti ini:

```python
match points:
    case []:
        print("No points")
    case [Point(0, 0)]:
        print("The origin")
    case [Point(x, y)]:
        print(f"Single point {x}, {y}")
    case [Point(0, y1), Point(0, y2)]:
        print(f"Two on the Y axis at {y1}, {y2}")
    case _:
        print("Something else")
```

**4.7. Mendefinisikan Fungsi**

Kita dapat membuat fungsi dengan contoh program Fibonacci ke batas acak arbitrary:

```python
>>> def fib(n):    # tulis deret fibonacci hingga n
...     """Print a Fibonacci series up to n."""
...     a, b = 0, 1
...     while a < n:
...         print(a, end=' ')
...         a, b = b, a+b
...     print()
...
>>> # Sekarang panggil fungsi yang baru saja kita definisikan:
... fib(2000)
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597
```

Kata kunci def merupakan keyword yang digunakan untuk menyatakn suatu fungsi pada program python. ... Fungsi adalah blok kode yang terorganisir dengan baik sehingga suatu saat kita dapat menggunakan nya kembali(reusable).

Definisi fungsi mengasosiasikan nama fungsi dengan objek fungsi dalam tabel simbol saat ini. Sebuah interpreter dapat mengenali objek yang ditunjuk dengan nama itu sebagai fungsi yang ditentukan oleh pengguna.

```python
>>> fib
<function fib at 10042ed0>
>>> f = fib
>>> f(100)
0 1 1 2 3 5 8 13 21 34 55 89
```

Sangat mudah untuk menulis fungsi yang mengembalikan daftar list nomor seri Fibonacci, seperti:

```python
>>> def fib2(n):  # return Fibonacci series up to n
...     """Return a list containing the Fibonacci series up to n."""
...     result = []
...     a, b = 0, 1
...     while a < n:
...         result.append(a)    # see below
...         a, b = b, a+b
...     return result
...
>>> f100 = fib2(100)    # call it
>>> f100                # write the result
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
```

* Pernyataan return kembali dengan nilai dari suatu fungsi. return tanpa argumen ekspresi mengembalikan None. Keluar dari akhir suatu fungsi juga mengembalikan None.

* Pernyataan result.append(a) memanggil method dari objek daftar list result. Sebuah metode adalah fungsi yang 'milik' sebuah objek dan dinamai `obj.methodname`, di mana `obj` adalah suatu objek (ini mungkin sebuah ekspresi), dan `methodname` adalah nama dari metode yang ditentukan oleh tipe objek.

**4.8. Lebih lanjut tentang Mendefinisikan Fungsi**

Dimungkinkan juga untuk mendefinisikan fungsi dengan sejumlah variabel argumen. Ada tiga bentuk, yang bisa digabungkan.

**4.8.1. Nilai Argumen Bawaan (default)**

Bentuk yang paling berguna adalah menentukan nilai default untuk satu atau lebih argumen. Hal tersebut menciptakan fungsi yang bisa dipanggil dengan argumen yang lebih sedikit daripada yang didefinisikan untuk diizinkan. Sebagai contoh:

```python
def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
```

Nilai default dievaluasi pada titik definisi fungsi dalam ruang lingkum yang telah ditentukan, seperti:

```python
i = 5

def f(arg=i):
    print(arg)

i = 6
f()
```

Fungsi bawaan (default) membuat perbedaan ketika bawaan adalah objek yang dapat diubah seperti daftar list, kamus dictionary, atau instances. Di mana fungsi default akan mengakumulasi argumen yang diteruskan, contohnya:

```python
def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# Output
[1]
[1, 2]
[1, 2, 3]
```

**4.8.2. Argumen Kata Kunci Keyword Arguments**

Fungsi juga dapat dipanggil menggunakan keyword argument dari bentuk `kwarg=value`. Misalnya, fungsi berikut:

```python
def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")
```

menerima satu argumen yang diperlukan (voltage) dan tiga argumen opsional (state, action, dan type). Fungsi ini dapat dipanggil dengan salah satu cara berikut:

```python
parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword
```

Dalam pemanggilan fungsi, argumen kata kunci keyword argument harus mengikuti argumen posisi. Semua argumen kata kunci keyword argument yang diteruskan harus cocok dengan salah satu argumen yang diterima oleh fungsi, dan urutannya tidak penting.

Misalnya, jika kita mendefinisikan fungsi seperti ini:

```python
def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

# Output

-- Do you have any Limburger ?
-- I'm sorry, we're all out of Limburger
It's very runny, sir.
It's really very, VERY runny, sir.
----------------------------------------
shopkeeper : Michael Palin
client : John Cleese
sketch : Cheese Shop Sketch
```

**4.8.3. Parameter spesial**

Secara bawaan, argumen dapat diteruskan ke fungsi Python baik dengan posisi atau secara eksplisit oleh kata kunci. Untuk keterbacaan dan kinerja, masuk akal untuk membatasi cara argumen dapat dilewatkan sehingga pengembang hanya perlu melihat definisi fungsi untuk menentukan apakah item dilewatkan secara posisi saja, posisi atau kata kunci.

Definisi fungsi mungkin terlihat seperti:

```python
def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):
      -----------    ----------     ----------
        |             |                  |
        |        Positional or keyword   |
        |                                - Keyword only
         -- Positional only
```

di mana `/` dan `*` adalah opsional. Jika digunakan, simbol-simbol ini menunjukkan jenis parameter dengan cara argumen dilewatkan ke fungsi.

Jika `positional-only`, urutan parameter penting, dan parameter tidak dapat dilewatkan dengan (keyword) kata kunci. Parameter `positional-only` ditempatkan sebelum `/` (garis miring). `/` Digunakan untuk secara logis memisahkan parameter `positional-only` dari parameter lainnya. Jika tidak ada `/` dalam definisi fungsi, tidak ada parameter `positional-only`.

Parameter yang mengikuti `/` dapat berupa `positional-or-keyword` atau `keyword-only`.

Untuk menandai parameter sebagai `keyword-only`, yang menunjukkan parameter harus dilewatkan dengan argumen (keyword) kata kunci, tempatkan `*` dalam daftar argumen tepat sebelum parameter `keyword-only`.

Berikut merupakan contoh program:

```python
>>> def standard_arg(arg):
...     print(arg)
...
>>> def pos_only_arg(arg, /):
...     print(arg)
...
>>> def kwd_only_arg(*, arg):
...     print(arg)
...
>>> def combined_example(pos_only, /, standard, *, kwd_only):
...     print(pos_only, standard, kwd_only)
```

* fungsi pertama `standard_arg` merupakan bentuk yang standard, tidak membatasi konvensi pemanggilan dan argumen dapat diteruskan oleh posisi atau kata kunci. contohnya:

```python
>>> standard_arg(2)
2

>>> standard_arg(arg=2)
2
```

* Fungsi kedua `pos_only_arg` dibatasi hanya menggunakan parameter posisi karena ada `/` dalam definisi fungsi.

```python
>>> pos_only_arg(1)
1

>>> pos_only_arg(arg=1)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: pos_only_arg() got some positional-only arguments passed as keyword arguments: 'arg'
```

* Fungsi ketiga `kwd_only_args` hanya mengizinkan argumen kata kunci seperti yang ditunjukkan oleh `a` dalam definisi fungsi.

```python
>>> kwd_only_arg(3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: kwd_only_arg() takes 0 positional arguments but 1 was given

>>> kwd_only_arg(arg=3)
3
```
* menggunakan ketiga konvensi pemanggilan dalam definisi fungsi yang sama.

```python
>>> combined_example(1, 2, 3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() takes 2 positional arguments but 3 were given

>>> combined_example(1, 2, kwd_only=3)
1 2 3

>>> combined_example(1, standard=2, kwd_only=3)
1 2 3

>>> combined_example(pos_only=1, standard=2, kwd_only=3)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: combined_example() got some positional-only arguments passed as keyword arguments: 'pos_only'
```

```python
>>> foo(1, **{'name': 2})
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: foo() got multiple values for argument 'name'
>>>

def foo(name, /, **kwds):
    return 'name' in kwds
>>> foo(1, **{'name': 2})
True
```

Sebagai pedoman:

* Gunakan `positional-only` jika Anda ingin nama parameter tidak tersedia bagi pengguna. Ini berguna ketika nama parameter tidak memiliki arti nyata, jika Anda ingin menegakkan urutan argumen ketika fungsi dipanggil atau jika Anda perlu mengambil beberapa parameter posisi dan kata kunci bergantian arbitrary.

* Gunakan `keyword-only` ketika nama memiliki makna dan definisi fungsi lebih mudah dipahami dengan secara eksplisit menggunakan nama atau Anda ingin mencegah pengguna mengandalkan posisi argumen yang dikirimkan.

* Untuk API, gunakan `positional-only` untuk mencegah perubahan yang merusak dari API jika nama parameter diubah di masa mendatang.

**4.8.4 Arbitrary Argument Lists**

menentukan bahwa suatu fungsi dapat dipanggil dengan sejumlah argumen yang berubah-ubah. Argumen-argumen ini akan dibungkus dalam sebuah tuple (lihat tuttuples). Sebelum jumlah variabel argumen, nol atau lebih argumen normal dapat muncul.

```python
def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))
```

Biasanya, argumen `variadic` ini akan menjadi yang terakhir dalam daftar parameter formal, karena mereka mengambil semua argumen masukan yang tersisa yang diteruskan ke fungsi. Parameter formal apa pun yang muncul setelah parameter `*args` adalah argumen `keyword-only`, yang berarti bahwa parameter itu hanya dapat digunakan sebagai `keyword` daripada argumen `posisi`.

```python
>>> def concat(*args, sep="/"):
...     return sep.join(args)
...
>>> concat("earth", "mars", "venus")
'earth/mars/venus'
>>> concat("earth", "mars", "venus", sep=".")
'earth.mars.venus'
```

**4.8.5 Unpacking Argument Lists**

Ketika argumen sudah ada dalam daftar list atau tuple tetapi perlu dibongkar untuk panggilan fungsi yang membutuhkan argumen posisi terpisah. Sebagai contoh, fungsi bawaan `range()` mengharapkan argumen terpisah start dan stop. Jika tidak tersedia secara terpisah, tulis fungsi panggilan dengan operator `*` untuk membongkar argumen dari daftar list atau tuple:

```python
>>> list(range(3, 6))            # normal call with separate arguments
[3, 4, 5]
>>> args = [3, 6]
>>> list(range(*args))            # call with arguments unpacked from a list
[3, 4, 5]
```

atau bisa menggunakan argumen `keyword` dengan operator `**`:

```python
>>> def parrot(voltage, state='a stiff', action='voom'):
...     print("-- This parrot wouldn't", action, end=' ')
...     print("if you put", voltage, "volts through it.", end=' ')
...     print("E's", state, "!")
...
>>> d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
>>> parrot(**d)
-- This parrot wouldn't VOOM if you put four million volts through it. E's bleedin' demised !
```

**4.8.6. Ekspresi Lambda**

Dalam python terdapat Ekspresi lambda atau fungsi lambda. Di mana fungsi ini dapat mengembalikan jumlah dari dua argumennya contohnya: `lambda a, b: a+b`. Fungsi Lambda dapat digunakan di mana pun objek fungsi diperlukan dan dapat mereferensikan variabel dari cakupan. di bawah adalah contoh ekspresi lambda untuk pengembalian fungsi:

```python
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```

Penggunaan lain adalah untuk melewatkan fungsi kecil sebagai argumen:

```python
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

**4.8.7. String Dokumentasi**

Pada Python ada beberapa konvensi tentang konten dan format string dokumentasi.

* Baris pertama harus selalu berupa ringkasan singkat dan ringkas dari tujuan objek. Untuk singkatnya, itu tidak boleh secara eksplisit menyatakan nama atau jenis objek, karena ini tersedia dengan cara lain (kecuali jika nama tersebut merupakan kata kerja yang menggambarkan operasi fungsi). Baris ini harus dimulai dengan huruf kapital dan diakhiri dengan titik.

* Jika ada lebih banyak baris dalam string dokumentasi, baris kedua harus kosong, memisahkan ringkasan secara visual dari sisa deskripsi. Baris berikut harus satu atau lebih paragraf yang menggambarkan konvensi pemanggilan objek, efek sampingnya, dll.

Berikut adalah contoh dari multi-baris docstring:

```python
>>> def my_function():
...     """Do nothing, but document it.
...
...     No, really, it doesn't do anything.
...     """
...     pass
...
>>> print(my_function.__doc__)
Do nothing, but document it.

    No, really, it doesn't do anything.
```

**4.8.8. Anotasi Fungsi**

Anotasi Fungsi informasi metadata yang sepenuhnya opsional tentang jenis yang digunakan oleh fungsi yang ditentukan pengguna. Anotasi disimpan dalam atribut `__annotations__` dari fungsi sebagai kamus dan tidak berpengaruh pada bagian lain dari fungsi tersebut. Anotasi parameter ditentukan oleh titik dua setelah nama parameter, diikuti dengan ekspresi yang mengevaluasi nilai anotasi. Anotasi pengembalian didefinisikan oleh literal `->`, diikuti oleh ekspresi, antara daftar parameter dan titik dua yang menunjukkan akhir dari pernyataan def. Contoh berikut memiliki argumen yang diperlukan, argumen opsional, dan nilai kembalian yang dianotasi:

```python
>>> def f(ham: str, eggs: str = 'eggs') -> str:
...     print("Annotations:", f.__annotations__)
...     print("Arguments:", ham, eggs)
...     return ham + ' and ' + eggs
...
>>> f('spam')
Annotations: {'ham': <class 'str'>, 'return': <class 'str'>, 'eggs': <class 'str'>}
Arguments: spam eggs
'spam and eggs'
```

**4.9. Intermezzo: Gaya Coding**

Sebagian besar bahasa dapat ditulis (atau lebih ringkas, formatted) dalam gaya yang berbeda; beberapa lebih mudah dibaca daripada yang lain. Memudahkan orang lain untuk membaca kode Anda selalu merupakan ide yang baik, dan mengadopsi gaya pengkodean yang bagus sangat membantu untuk itu.

Untuk Python, PEP 8 telah muncul sebagai sebuah panduan gaya penulisan kode yang mudah dibaca. Pada python ada poin paling penting yang ditunjukkan seperti:

* Gunakan lekukan 4-spasi, dan tanpa tab. 4 spasi adalah kompromi yang baik antara indentasi kecil (memungkinkan kedalaman bersarang lebih besar) dan indentasi besar (lebih mudah dibaca). Tab menimbulkan kebingungan, dan sebaiknya ditinggalkan.

* Bungkus wrap garis agar tidak melebihi 79 karakter. Ini membantu pengguna dengan tampilan kecil dan memungkinkan untuk memiliki beberapa file kode berdampingan pada tampilan yang lebih besar.

* Gunakan baris kosong untuk memisahkan fungsi dan kelas, dan blok kode yang lebih besar di dalam fungsi.

* Jika memungkinkan, berikan komentar pada baris terkait.

* Gunakan String Dokumentasi docstrings.

* Gunakan spasi di sekitar operator dan setelah koma, tetapi tidak secara langsung di dalam konstruksi kurung bracketing: `a = f(1, 2) + g(3, 4)`.

* Beri nama kelas dan fungsi Anda secara konsisten; konvensi ini menggunakan UpperCamelCase untuk kelas dan `lowercase_with_underscores` untuk fungsi dan metode. Selalu gunakan self sebagai nama untuk argumen metode pertama.

* Jangan gunakan pengkodean ajaib fancy encodings jika kode Anda dimaksudkan untuk digunakan di lingkungan internasional. Default Python, UTF-8, atau bahkan ASCII biasa berfungsi paling baik dalam hal apa pun.

* Demikian juga, jangan gunakan karakter non-ASCII dalam pengidentifikasi jika hanya ada sedikit kesempatan orang berbicara bahasa yang berbeda akan membaca atau merawat kode.