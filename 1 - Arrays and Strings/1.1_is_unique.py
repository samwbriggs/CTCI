# Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional
# data structures?

def is_unique(s: str) -> bool:
    # Most efficient solution would be using a dictionary (hash table).
    # An array of booleans would also work where the index is equal to the ASCII value of the character.

    # If we aren't allowed to use additional data structures we can loop through each character and see if it exists
    # within the same string which would take O(n^2) time. We could also sort the string and see if neighboring characters
    # are equal to each other which would likely take O(n log n) time.

    charsSeen = {}
    for char in s:
        if char in charsSeen:
            charsSeen[char] += 1
            if charsSeen[char] > 1:
                return False
        else:
            charsSeen[char] = 1

    return True

result: bool = is_unique("apple")
print(result)