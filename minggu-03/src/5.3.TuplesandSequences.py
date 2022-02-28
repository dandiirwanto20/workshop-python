t = 12345, 54321, 'hello!'
t[0]
# 12345 (Output)
t
# (12345, 54321, 'hello!') (Output)

# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
u
# ((12345, 54321, 'hello!'), (1, 2, 3, 4, 5)) (Output)

# Tuples are immutable:
t[0] = 88888
# Traceback (most recent call last): (Output)
#   File "<stdin>", line 1, in <module> (Output)
# TypeError: 'tuple' object does not support item assignment (Output)

# but they can contain mutable objects:
v = ([1, 2, 3], [3, 2, 1])
v
# ([1, 2, 3], [3, 2, 1]) (Output)