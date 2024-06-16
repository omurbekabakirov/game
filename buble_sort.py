from random import randint
def bubble_sort(lst):
    lst = [randint(1, 1000) for _ in range(5)]
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
random_numbers = bubble_sort([])
print("Sorted List:", random_numbers)
