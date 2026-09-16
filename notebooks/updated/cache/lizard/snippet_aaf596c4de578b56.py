def get_random_name():
    char_seq = []
    name_source = random.randint(1, 2 ** 8 - 1)
    current_value = name_source
    while current_value > 0:
        char_offset = current_value % 26
        current_value = current_value - random.randint(1, 26)
        char_seq.append(chr(char_offset + ord('a')))
    name = ''.join(char_seq)
    assert re.match(VALID_PACKAGE_RE, name)
    return name