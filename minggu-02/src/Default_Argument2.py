def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))

# [1] (Output)
# [1, 2] (Output)
# [1, 2, 3] (Output)

# Jika Anda tidak ingin bawaan dibagi dengan panggilan berikutnya, Anda dapat menulis fungsi seperti ini sebagai gantinya:
def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L