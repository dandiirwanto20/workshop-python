# Implement single quote and double quote
'spam eggs'  # single quotes
# 'spam eggs' (output)
'doesn\'t'  # use \' to escape the single quote...
# "doesn't" (output)
"doesn't"  # ...or use double quotes instead
# "doesn't" (output)
'"Yes," they said.'
# '"Yes," they said.' (output)
"\"Yes,\" they said."
# '"Yes," they said.' (output)
'"Isn\'t," they said.'
# '"Isn\'t," they said.' (output)

# Using spesial caracter '\' and print()
'"Isn\'t," they said.' 
# '"Isn\'t," they said.' (output)
print('"Isn\'t," they said.')
# "Isn't," they said. (output)
s = 'First line.\nSecond line.'  # \n means newline
s  # without print(), \n is included in the output
# 'First line.\nSecond line.' (output)
print(s)  # with print(), \n produces a new line
# First line. (output)
# Second line. (output)

# dont want use \ and using r before fisrt quote 
print('C:\some\name')  # here \n means newline!
# C:\some (output)
# ame (output)
print(r'C:\some\name')  # note the r before the quote
# C:\some\name (output)

# using ("""...""") concept
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 3 times 'un', followed by 'ium'
3 * 'un' + 'ium'

# string literals
'Py' 'thon'
#'Python' (output)

text = ('Put several strings within parentheses '
         'to have them joined together.')
text
#'Put several strings within parentheses to have them joined together.' (output)

# This only works with two literals though, not with variables or expressions:
prefix = 'Py'
prefix 'thon'  # can't concatenate a variable and a string literal

# use + operator
prefix + 'thon'
# 'Python' (output)

#Strings can be indexed (subscripted)

word = 'Python'
word[0]  # character in position 0
# 'P' (output)
word[5]  # character in position 5
# 'n' (output)

# Indices may also be negative numbers, to start counting from the right:
word[-1]  # last character
# 'n' (output)
word[-2]  # second-last character
# 'o' (output)
word[-6]
# 'P' (output)

# In addition to indexing, slicing is also supported.
word[0:2]  # characters from position 0 (included) to 2 (excluded)
# 'Py' (output)
word[2:5]  # characters from position 2 (included) to 5 (excluded)
# 'tho' (output)

# Slice indices have useful defaults
word[:2]   # character from the beginning to position 2 (excluded)
# 'Py' (output)
word[4:]   # characters from position 4 (included) to the end
# 'on' (output)
word[-2:]  # characters from the second-last (included) to the end
# 'on' (output)

# Note how the start is always included, and the end always excluded.
word[:2] + word[2:]
# 'Python' (output)
word[:4] + word[4:]
# 'Python' (output)

# Attempting to use an index that is too large will result in an error:
word[42]  # the word only has 6 characters

# out of range slice indexes are handled gracefully when used for slicing
word[4:42]
# 'on' (output)
word[42:]
# '' (output)

# Python strings cannot be changed — they are immutable
word[0] = 'J' # error output
word[2:] = 'py' # error output

# If you need a different string, you should create a new one
'J' + word[1:]
# 'Jython' (output)
word[:2] + 'py'
# 'Pypy' (output)

# len() returns the length of a string:
s = 'supercalifragilisticexpialidocious'
len(s)
# 34 (output)