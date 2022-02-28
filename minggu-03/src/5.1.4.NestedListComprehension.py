matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
]

[[row[i] for row in matrix] for i in range(4)]
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] (Output)

# listcomp dievaluasi dalam konteks untuk yang mengikutinya, jadi contoh ini setara dengan:
transposed = []
for i in range(4):
         transposed.append([row[i] for row in matrix])
transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] (Output)

# Juga sama dengan:
transposed = []
for i in range(4):
    # the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
        transposed.append(transposed_row)
transposed
# [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]] (Output)

# Fungsi Zip() akan melakukan pekerjaan yang baik untuk kasus penggunaan ini:
list(zip(*matrix))
# [(1, 5, 9), (2, 6, 10), (3, 7, 11), (4, 8, 12)] (Output)