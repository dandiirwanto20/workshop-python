class Warehouse:
        purpose = 'storage'
        region = 'west'

w1 = Warehouse()
print(w1.purpose, w1.region)
# storage west (Output)
w2 = Warehouse()
w2.region = 'east'
print(w2.purpose, w2.region)
# storage east (Output)