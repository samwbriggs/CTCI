# There are three types of edits that can be performed on strings: insert a character,
# remove a character, or replace a character. Given two strings, write a function to check if they are
# one edit (or zero edits) away.

def one_away(s1: str, s2: str) -> bool:
    # Are all letters the same except one?
    # Do the letters occur the same number of times offset by one (remove/insert character)?

    # This block saves us from a O(n + m) runtime. Any strings that pass this check will be (if not nearly) the same length.
    lenDiff = abs(len(s1) - len(s2))
    if lenDiff > 1:
        return False

    # Use a dictionary to track character counts.
    charMap: dict = {}
    for char in s1:
        if char in charMap:
            charMap[char] += 1
        else:
            charMap[char] = 1

    # Offset character counts with the second string.
    for char in s2:
        if char in charMap:
            charMap[char] -= 1
        else:
            charMap[char] = -1

    # If character counts exist in the dictionary, we need to track them and ensure they are either off by one or zero.
    charsDifferent: int = 0
    for char in charMap:
        if charMap[char] < 0 or charMap[char] > 0:
            charsDifferent += abs(charMap[char])
    
    if charsDifferent == 1 or charsDifferent == 0:
        return True
    
    return False

result: bool = one_away("pale", "bake")
print(result)