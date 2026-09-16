def hex_decode(input, errors='strict'):
    assert errors == 'strict'
    output = binascii.a2b_hex(''.join(char for char in input if char in
        hexdigits))
    return output, len(input)