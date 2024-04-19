# Implement a method to perform basic string compression using the counts
# of repeated characters. For example, the string aabcccccaaa would become a2blc5a3. If the
# "compressed" string would not become smaller than the original string, your method should return
# the original string. You can assume the string has only uppercase and lowercase letters (a - z).

def string_compression(s: str) -> str:
    # Is the string sorted?
    # Do uppercase and lowercase count as the same character?

    charNewLetter: list[str] = []
    charCountNewLetter: list[int] = []
    prevChar: str = ""
    newLetterIndex: int = -1
    for char in s:
        if prevChar == char:
            charCountNewLetter[newLetterIndex] += 1
        else:
            prevChar = char
            newLetterIndex += 1
            charNewLetter.insert(newLetterIndex, char)
            charCountNewLetter.insert(newLetterIndex, 1)

    if len(charNewLetter) == len(s):
        return s

    compressedStr: str = ""
    for index, char in enumerate(charNewLetter):
        compressedStr = "".join([compressedStr, charNewLetter[index], str(charCountNewLetter[index])])

    return compressedStr

compressedStr: str = string_compression("aabccdeeaa")
print(compressedStr)
