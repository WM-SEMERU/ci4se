def crude_tokenizer(line):
    tokens = []
    buffer = ''
    for c in line.strip():
        if c == ' ' or c in string.punctuation:
            if buffer:
                tokens.append(buffer)
                buffer = ''
        else:
            buffer += c
    if buffer:
        tokens.append(buffer)
    return tokens