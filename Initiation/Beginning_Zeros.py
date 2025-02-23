def beginning_zeros(a: str) -> int:
    # your code here
    zeros = 0
    for c in a:
        if c == '0':
            zeros += 1
        elif c != '0':
            break
    return zeros

print("Example:")
print(beginning_zeros("10"))

# These "asserts" are used for self-checking
assert beginning_zeros("100") == 0
assert beginning_zeros("001") == 2
assert beginning_zeros("100100") == 0
assert beginning_zeros("001001") == 2
assert beginning_zeros("012345679") == 1
assert beginning_zeros("0000") == 4

print("The mission is done! Click 'Check Solution' to earn rewards!")
