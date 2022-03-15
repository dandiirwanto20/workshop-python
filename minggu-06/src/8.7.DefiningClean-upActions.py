try:
     raise KeyboardInterrupt
finally:
     print('Goodbye, world!')
     
# Output:
"""
Goodbye, world!
KeyboardInterrupt
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
"""