tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel
# {'jack': 4098, 'sape': 4139, 'guido': 4127} (Output)
tel['jack']
# 4098 (Output)
del tel['sape']
tel['irv'] = 4127
tel
# {'jack': 4098, 'guido': 4127, 'irv': 4127} (Output)
list(tel)
# ['jack', 'guido', 'irv'] (Output)
sorted(tel)
# ['guido', 'irv', 'jack'] (Output)
'guido' in tel
# True (Output)
'jack' not in tel
# False (Output)