# Assume you have a method isSubstring which checks if one word is a substring
# of another. Given two strings, s1 and s2, write code to check if s2 is a rotation of s1 using only one
# call to isSubstring (e.g., "waterbottle" is a rotation of"erbottlewat").

def is_rotation(s1: str, s2: str) -> bool:
    # Concatenate s1 onto itself.
    # Call isSubstring on the concatenated string with the other and see if it exists.

    # If strings are not the same length it cannot be a rotation.
    if len(s1) != len(s2):
        return False

    double: str = "".join([s1, s1])
    if is_substring(s2, double):
        # If we find the entire occurence of s2 inside our doubled string, we know it's a rotation.
        return True

    return False

def is_substring(s1: str, s2: str) -> bool:
    # Magic imaginary method to determine if one string is a substring of another.
    return False