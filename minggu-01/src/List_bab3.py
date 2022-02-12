squares = [1, 4, 9, 16, 25]
squares
# [1, 4, 9, 16, 25] (output)

# Like strings (and all other built-in sequence types), lists can be indexed and sliced:
squares[0]  # indexing returns the item
# 1 (output)
squares[-1]
# 25 (output)
squares[-3:]  # slicing returns a new list
# [9, 16, 25] (output)

# All slice operations return a new list containing the requested elements. This means that the following slice returns a shallow copy of the list:
squares[:]
# [1, 4, 9, 16, 25] (output)

#Lists also support operations like concatenation:
squares + [36, 49, 64, 81, 100]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100] (output)

# Unlike strings, which are immutable, lists are a mutable type, i.e. it is possible to change their content:
cubes = [1, 8, 27, 65, 125]  # something's wrong here
4 ** 3  # the cube of 4 is 64, not 65!
# 64 (output)
cubes[3] = 64  # replace the wrong value
cubes 
# [1, 8, 27, 64, 125] (output)

# You can also add new items at the end of the list, by using the append() method (we will see more about methods later):
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
cubes
# [1, 8, 27, 64, 125, 216, 343] (output)

# Assignment to slices is also possible, and this can even change the size of the list or clear it entirely:
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters
# ['a', 'b', 'c', 'd', 'e', 'f', 'g'] (output)

# replace some values
letters[2:5] = ['C', 'D', 'E']
letters
# ['a', 'b', 'C', 'D', 'E', 'f', 'g'] (output)

# now remove them
letters[2:5] = []
letters
# ['a', 'b', 'f', 'g'] (output)

# clear the list by replacing all the elements with an empty list
letters[:] = []
letters
# [] (output)

# The built-in function len() also applies to lists:
letters = ['a', 'b', 'c', 'd']
len(letters)
# 4 (output)

# It is possible to nest lists (create lists containing other lists), for example:
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
x
# [['a', 'b', 'c'], [1, 2, 3]] (output)

x[0]

# ['a', 'b', 'c'] (output)

x[0][1]
# 'b' (output)