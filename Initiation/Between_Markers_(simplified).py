def between_markers(text: str, start: str, end: str) -> str:
    # your code here
    index_start = text.find(start) + 1
    index_end = text.find(end)
    if index_end > index_start:
        return text[index_start:index_end]
    return ""


print("Example:")
print(between_markers("What is >apple<", ">", "<"))

# These "asserts" are used for self-checking
assert between_markers("What is >apple<", ">", "<") == "apple"
assert between_markers("What is [apple]", "[", "]") == "apple"
assert between_markers("What is ><", ">", "<") == ""
assert between_markers("[an apple]", "[", "]") == "an apple"

print("The mission is done! Click 'Check Solution' to earn rewards!")
