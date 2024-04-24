# Write a method to replace all spaces in a string with '%20'. You may assume that the string 
# has sufficient space at the end to hold the additional characters, and that you are given the "true" 
# length of the string. (Note: If implementing in Java, please use a character array so that you can 
# perform this operation in place.)

def URLify(s: list[str]) -> str:
    sCopy: str = "".join(s)
    sOffset: int = 0
    for i in range(len(s)):
        if i + sOffset > len(s) - 1:
            break
        
        if sCopy[i] == ' ':
            s[i+sOffset] = '%'
            s[i+sOffset+1] = '2'
            s[i+sOffset+2] = '0'
            sOffset += 2
        else:
            s[i+sOffset] = sCopy[i]

    return s

result: list[str] = URLify(list("www.youtube.com/Charlie Bit my Finger/      "))
print("".join(result))