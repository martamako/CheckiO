from typing import Iterable


def split_pairs(text: str) -> Iterable[str]:
    # your code here
    pairs = []
    while len(text) > 1:
        pairs.append(text[:2])
        text = text[2:]
    if len(text) == 0:
        return pairs
    pairs.append(text[:1] + '_')
    return pairs


print("Example:")
print(list(split_pairs("abcd")))

assert list(split_pairs("abcd")) == ["ab", "cd"]
assert list(split_pairs("abc")) == ["ab", "c_"]
assert list(split_pairs("abcdf")) == ["ab", "cd", "f_"]
assert list(split_pairs("a")) == ["a_"]
assert list(split_pairs("")) == []

print("The mission is done! Click 'Check Solution' to earn rewards!")
