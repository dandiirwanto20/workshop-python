def fib(n):    # write Fibonacci series up to n
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

# Now call the function we just defined:
fib(2000)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 (Output)

fib

f = fib
f(100)
# 0 1 1 2 3 5 8 13 21 34 55 89 (Output)

fib(0)
print(fib(0))
# None (Output)

