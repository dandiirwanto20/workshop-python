basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # tunjukkan bahwa duplikat telah dihapus
# {'orange', 'banana', 'pear', 'apple'} (Output)
'orange' in basket                 # pengujian keanggotaan cepat
# True (Output)
'crabgrass' in basket
# False (Output)

# Peragakan operasi himpunan pada huruf unik dari dua kata
a = set('abracadabra')
b = set('alacazam')
a                                  # huruf unik dalam a
# {'a', 'r', 'b', 'c', 'd'} (Output)
a - b                              # huruf di a tapi tidak di b
# {'r', 'd', 'b'} (Output)
a | b                              # huruf dalam a atau b atau keduanya
# {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'} (Output)
a & b                              # huruf a dan b
# {'a', 'c'} (Output)
a ^ b                              # huruf a atau b tapi tidak keduanya
# {'r', 'd', 'b', 'm', 'z', 'l'} (Output)