arr = [33,22,66,77,88]

n = arr[2]

arr[3] = 345

print(arr)

for x in arr:
    print(x)

for y in arr:
    print(y*y)

for z in arr:
    if z%2 == 0:
        print(z)

i = 0
while i<len(arr):
    print(arr[i])
    i += 1

"""

tablica ma wartości jednego typu. Lista może mieć różnego

arr=[1,2,3]
lista1=[1,2,False,"4"]

Przy przetwarzaniu dużych list może być problem i wtedy lepsze są tablice

Caly czas używamy list

"""