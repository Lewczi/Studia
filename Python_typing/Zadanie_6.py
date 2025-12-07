def process_lists(list1: list[int], list2: list[int]) -> list[int]:

    merged = list1 + list2
    unique = list(set(merged))
    cubed = [x ** 3 for x in unique]
    return cubed


l1 = [1, 5, 2]
l2 = [2, 3, 4]

print(process_lists(l1, l2))
