from random import randint


def bubble_sort():
    lst = [randint(1, 1000) for _ in range(5)]
    print(f"The list{lst}")
    n = len(lst)
    for i in range(n):
        for j in range(0,   n - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                print(lst)


bubble_sort()
