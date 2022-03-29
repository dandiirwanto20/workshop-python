s = 'abc'
it = iter(s)
it
# <str_iterator object at 0x10c90e650>
next(it)
# 'a' (Output)
next(it)
# 'b' (Output)
next(it)
# 'c' (Output)
next(it)

# Output
"""
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    next(it)
StopIteration
"""