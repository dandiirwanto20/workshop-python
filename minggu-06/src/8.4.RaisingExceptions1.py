# memanggil pembangunnya constructor tanpa argumen:
# raise ValueError  # singkatan untuk 'raise ValueError()'

try:
     raise NameError('HiThere')
except NameError:
     print('An exception flew by!')
     raise

# Output
"""
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
NameError: HiTh
"""