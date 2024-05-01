# Given two strings, write a method to decide if one is a permutation of the other.

def check_permutation(s1: str, s2: str) -> bool:
    # Is the permutation case-sensitive?
    # Does white space count as a character?

    # Use a hash table and ensure each character appears the same amount of times in the other string.

    if len(s1) != len(s2): return False

    charCount = {}
    for char in s1:
        if char in charCount:
            charCount[char] += 1
        else:
            charCount[char] = 1

    for char in s2:
        if char in charCount:
            charCount[char] -= 1
            if charCount[char] < 0:
                return False
        else:
            return False
        
    return True

result: bool = check_permutation("stars", "tarss")
print(result)