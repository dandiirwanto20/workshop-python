for n in range(2, 10):
    for x in range(2, n):
        if n % x == 0:
            print(n, 'equals', x, '*', n//x)
            break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')

# 2 is a prime number (Output)
# 3 is a prime number (Output)
# 4 equals 2 * 2 (Output)
# 5 is a prime number (Output)
# 6 equals 2 * 3 (Output)
# 7 is a prime number (Output)
# 8 equals 2 * 4 (Output)
# 9 equals 3 * 3 (Output)