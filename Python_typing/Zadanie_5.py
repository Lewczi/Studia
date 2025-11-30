def wartosci(items: list[int], value: int) -> bool:
    return value in items

my_list = [1, 2, 3, 4, 5]
print(wartosci(my_list, 3))