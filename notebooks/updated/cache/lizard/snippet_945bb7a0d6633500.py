def hex_to_unichr(hex_string):
    if hex_string is None or len(hex_string) < 1:
        return None
    if hex_string.startswith('U+'):
        hex_string = hex_string[2:]
    return int_to_unichr(int(hex_string, base=16))