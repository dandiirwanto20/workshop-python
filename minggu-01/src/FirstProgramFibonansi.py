# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# Strings are printed without quotes, and a space is inserted between items, so you can format things nicely, like this:
i = 256*256
print('The value of i is', i)

# The keyword argument end can be used to avoid the newline after the output, or end the output with a different string:
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b