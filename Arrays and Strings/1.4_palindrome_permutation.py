# Given a string, write a function to check if it is a permutation of a palindrome.
# A palindrome is a word or phrase that is the same forwards and backwards. A permutation
# is a rearrangement of letters. The palindrome does not need to be limited to just dictionary words.

def palindrome_permutation(s: str) -> bool:
    # All palindromes must have an even amount of each character with the exception of the middle character if the length of the
    # string is odd. If more than one character occurs an odd number of times we know this string is an invalid palindrome permutation.

    # Make all letters lowercase and remove any whitespaces.
    s = s.lower().replace(" ", "")

    # Fill a dictionary (hashtable) with the occurrences of each letter.
    charHash = {}
    for char in s:
        if char in charHash:
            charHash[char] += 1
        else:
            charHash[char] = 1

    # Loop through the dictionary. Track the number of odd occurrences for a character. If there are more than one characters with an
    # odd count, this is not a valid palindrome permutation.
    oddNumOfChars = 0
    for char in charHash:
        if charHash[char] % 2 > 0:
            oddNumOfChars += 1
            if oddNumOfChars > 1:
                return False
    
    return True

result: bool = palindrome_permutation("tactcoapapa")
print(result)