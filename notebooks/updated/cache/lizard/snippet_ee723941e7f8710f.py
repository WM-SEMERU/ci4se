def match_alphabet(self, pattern):
    s = {}
    for char in pattern:
        s[char] = 0
    for i in range(len(pattern)):
        s[pattern[i]] |= 1 << len(pattern) - i - 1
    return s