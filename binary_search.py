def binary_search(a, value):
    global Pos
    n = 5000
    result_ok = False
    first = 0
    last = n - 1
    while first <= last:
        mid = (first + last) // 2
        if value == a[mid]:
            result_ok = True
            Pos = mid
            break
        elif a[mid] < value:
            first = mid + 1

        elif a[mid] > value:
            last = mid - 1

    if result_ok:
        return f'Element found at index {Pos}'
    else:
        return 'Element not found'


A = list(range(1, 5000))
result = binary_search(A, 38)
print(result)
