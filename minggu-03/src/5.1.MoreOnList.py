fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
fruits.count('apple')
# 2 (Output)
fruits.count('tangerine')
# 0 (Output)
fruits.index('banana')
# 3 (Output)
fruits.index('banana', 4)  # Find next banana starting a position 4
# 6 (Output)
fruits.reverse()
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange'] (Output)
fruits.append('grape')
fruits
# ['banana', 'apple', 'kiwi', 'banana', 'pear', 'apple', 'orange', 'grape'] (Output)
fruits.sort()
fruits
# ['apple', 'apple', 'banana', 'banana', 'grape', 'kiwi', 'orange', 'pear'] (Output)
fruits.pop()
# 'pear' (Output)