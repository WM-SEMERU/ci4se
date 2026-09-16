def nth_char(char_map, index):
    for char in char_map:
        if index < char_map[char]:
            return char
        index = index - char_map[char]
    return None