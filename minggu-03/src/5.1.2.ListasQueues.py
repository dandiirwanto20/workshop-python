from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry tiba
queue.append("Graham")          # Graham tiba
queue.popleft()                 # Yang pertama tiba sekarang pergi
# 'Eric'
queue.popleft()                 # Yang kedua tiba sekarang pergi
# 'John'
queue                           # Antrian yang tersisa sesuai urutan kedatangan
# deque(['Michael', 'Terry', 'Graham'])