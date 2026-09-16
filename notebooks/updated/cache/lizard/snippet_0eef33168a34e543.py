def parse_dict_strings(code):
    i = 0
    level = 0
    chunk_start = 0
    curr_paren = None
    for i, char in enumerate(code):
        if char in ['(', '[', '{'] and curr_paren is None:
            level += 1
        elif char in [')', ']', '}'] and curr_paren is None:
            level -= 1
        elif char in ['"', "'"]:
            if curr_paren == char:
                curr_paren = None
            elif curr_paren is None:
                curr_paren = char
        if level == 0 and char in [':', ','] and curr_paren is None:
            yield code[chunk_start:i].strip()
            chunk_start = i + 1
    yield code[chunk_start:i + 1].strip()