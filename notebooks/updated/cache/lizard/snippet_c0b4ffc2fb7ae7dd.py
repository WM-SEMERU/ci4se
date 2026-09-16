def pack_iterable(messages):
    return pack_string(struct.pack('>l', len(messages)) + ''.join(map(
        pack_string, messages)))