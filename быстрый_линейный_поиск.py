from datetime import datetime


def liner_search(lst, x):
    i = 0
    count = len(lst)
    lst.append(x)
    while True:
        if lst[i] == x:
            del lst[count]
            return i if i < count else None

        i += 1


items = [2, 3, 5, 7, 11, 13, 17]
print(liner_search(items, 1))  # None
print(liner_search(items, 7))  # 3
print(liner_search(items, 19))  # None

print(items)

# *** simplified speed test ***

items = list(range(0, 1000000))
r_count = 100

start = datetime.now()

for n in range(1, r_count):
    liner_search(items, 777777)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds / r_count)
