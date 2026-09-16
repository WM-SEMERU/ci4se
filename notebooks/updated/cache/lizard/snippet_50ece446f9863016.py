def chunk_math(text):
    opened_braces = 0
    last_char = ''
    for char in text:
        if char == '{' and last_char != '\\':
            opened_braces += 1
        if char == '}' and last_char != '\\':
            opened_braces -= 1
            if opened_braces < 0:
                raise ValueError("Braces don't match: %s" % text)
        last_char = char
    if opened_braces != 0:
        raise ValueError('%i braces are still open' % opened_braces)
    single_symbol = ['_', '^', '&', '{', '}']
    breaking_chars = ['\\', ' '] + single_symbol
    chunks = []
    current_chunk = ''
    for char in text:
        if current_chunk == '':
            current_chunk = char
            continue
        if char == '\\':
            if current_chunk == '\\':
                current_chunk += char
                chunks.append(current_chunk)
                current_chunk = ''
            else:
                chunks.append(current_chunk)
                current_chunk = char
        elif current_chunk == '\\' and char in breaking_chars:
            current_chunk += char
            chunks.append(current_chunk)
            current_chunk = ''
        elif char in breaking_chars:
            chunks.append(current_chunk)
            current_chunk = char
        elif char in string.letters + string.digits and current_chunk[0
            ] == '\\':
            current_chunk += char
        else:
            chunks.append(current_chunk)
            current_chunk = char
    if current_chunk != '':
        chunks.append(current_chunk)
    filtered = []
    for chunk in chunks:
        if len(filtered) > 0 and filtered[-1] == ' ' and chunk == ' ':
            continue
        filtered.append(chunk)
    return filtered