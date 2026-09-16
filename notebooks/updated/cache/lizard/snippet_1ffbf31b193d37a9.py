def _mysql_aes_key(key):
    final_key = bytearray(16)
    for i, c in enumerate(key):
        final_key[i % 16] ^= key[i] if PY3 else ord(key[i])
    return bytes(final_key)