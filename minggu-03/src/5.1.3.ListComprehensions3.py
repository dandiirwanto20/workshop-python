vec = [-4, -2, 0, 2, 4]

# create a new list with the values doubled
[x*2 for x in vec]
# [-8, -4, 0, 4, 8] (Output)

# filter the list to exclude negative numbers
[x for x in vec if x >= 0]
# [0, 2, 4] (Output)

# apply a function to all the elements
[abs(x) for x in vec]
# [4, 2, 0, 2, 4] (Output)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
[weapon.strip() for weapon in freshfruit]
# ['banana', 'loganberry', 'passion fruit'] (Output)

# create a list of 2-tuples like (number, square)
[(x, x**2) for x in range(6)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16), (5, 25)] (Output)

# the tuple must be parenthesized, otherwise an error is raised
[x, x**2 for x in range(6)]
#   File "<stdin>", line 1, in <module> (Output)
#     [x, x**2 for x in range(6)] (Output)
#               ^ (Output)
# SyntaxError: invalid syntax (Output)

# flatten a list using a listcomp with two 'for'
vec = [[1,2,3], [4,5,6], [7,8,9]]
[num for elem in vec for num in elem]
# [1, 2, 3, 4, 5, 6, 7, 8, 9] (Output)