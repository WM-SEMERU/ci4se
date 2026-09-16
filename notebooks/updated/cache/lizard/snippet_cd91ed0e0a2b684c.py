def safe_split_index(string, max_len):
    last_index = get_last_certain_break_index(string, max_len)
    for l in grapheme_lengths(string[last_index:]):
        if last_index + l > max_len:
            break
        last_index += l
    return last_index