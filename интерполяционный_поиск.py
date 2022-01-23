from datetime import datetime


# works when the array is sorted
def interp_search(lst, x):
    low = 0
    high = len(lst) - 1

    while lst[low] < x < lst[high]:
        mid = low + ((x - lst[low]) * (high - low)) // (lst[high] - lst[low])

        if lst[mid] < x:
            low = mid + 1
        elif lst[mid] > x:
            high = mid - 1
        else:
            return mid

    if lst[low] == x:
        return low
    if lst[high] == x:
        return high

    return None


items = [2, 3, 5, 7, 11, 13, 17]
print(interp_search(items, 1))  # None
print(interp_search(items, 7))  # 3
print(interp_search(items, 19))  # None

# *** simplified speed test ***
items = range(0, 1000000)
count = 100

start = datetime.now()

for i in range(1, count):
    interp_search(items, 777777)

delta = datetime.now() - start
totalMicroseconds = delta.seconds * 1000000 + delta.microseconds

print(totalMicroseconds / count)
