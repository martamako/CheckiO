from collections.abc import Iterable


def replace_first(items: list) -> Iterable:
    # your code here
    if len(items) <= 1:
        return items
    items = items[1:] + [items[0]]
    return items


# These "asserts" are used for self-checking
print("Example:")
print(list(replace_first([1, 2, 3, 4])))

assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
assert replace_first([1]) == [1]
assert replace_first([]) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
