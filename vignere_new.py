def vignere(text,key):
    result = ""
    key = key.lower()
    for i, char in enumerate(text):
        shift = ord(key[i%len(key)]) - ord('a')
        result += chr((ord(char) - ord('a') + shift) % 26 + ord('a'))
    return result

print(vignere("hello","key"))