def pkcs7_pad(inp, block_size):
    val = block_size - len(inp) % block_size
    if val == 0:
        return inp + bytes([block_size]) * block_size
    else:
        return inp + bytes([val]) * val