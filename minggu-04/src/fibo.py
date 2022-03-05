# Fibonacci numbers module in Bab 6 Modules

def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()

def fib2(n):   # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
    return result

# import fibo (jalankan dalam interpreter python)

# fibo.fib(1000) (dijalankan dalam interpreter python)
# 0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 (Output yang ditampilkan)
# fibo.fib2(100) (dijalankan dalam interpreter python)
# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89] (Output yang ditampilkan)
# fibo.__name__ (dijalankan dalam interpreter python)
# 'fibo' (Output yang ditampilkan)