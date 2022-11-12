def binary_search_recursive(array, low, high, element):
    if high >= low:
        mid = (high + low) // 2
        print(array[mid])
        if array[mid] == element :
            return mid

        elif array[mid] > element:
            return binary_search_recursive(array, low, mid-1, element)
        else:
            return binary_search_recursive(array, mid + 1, high, element)
    else:
        return -1

from random import randint

arr = []
for _ in range(10):
    arr.append(randint(1,100))
arr.sort()

N = len(arr)
start = 0
target = arr[randint(0,N-1)]

print(arr)
print(target)

value = binary_search_recursive(arr, start, N-1, target)
print(value)
