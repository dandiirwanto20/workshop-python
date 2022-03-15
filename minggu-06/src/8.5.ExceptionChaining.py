# statement raise memungkinkan opsional yang memungkinkan pengecualian rantai.
# raise RuntimeError from exc

# Ini bisa berguna saat kita mengubah pengecualian:
def func():
     raise ConnectionError

try:
     func()
except ConnectionError as exc:
     raise RuntimeError('Failed to open database') from exc
     
# Output
"""
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
  File "<stdin>", line 2, in func
ConnectionError
"""

# Pengecualian di atas adalah penyebab langsung dari pengecualian berikut:
"""
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Failed to open database
"""