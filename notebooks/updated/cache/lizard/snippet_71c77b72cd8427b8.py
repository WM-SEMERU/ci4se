def is_text(fp_, blocksize=512):
    int2byte = (lambda x: bytes((x,))) if six.PY3 else chr
    text_characters = b''.join(int2byte(i) for i in range(32, 127)
        ) + b'\n\r\t\x0c\x08'
    try:
        block = fp_.read(blocksize)
    except AttributeError:
        try:
            with fopen(fp_, 'rb') as fp2_:
                block = fp2_.read(blocksize)
        except IOError:
            return False
    if b'\x00' in block:
        return False
    elif not block:
        return True
    try:
        block.decode('utf-8')
        return True
    except UnicodeDecodeError:
        pass
    nontext = block.translate(None, text_characters)
    return float(len(nontext)) / len(block) <= 0.3