cars = ['red', 'blue', 'black', 'black', 'black', 'red', 'blue', 'red', 'white']
from collections import Counter
c = Counter(cars)

print(c)
print(c['black'])