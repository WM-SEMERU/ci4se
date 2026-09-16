def _decode_hex(self, value):
    result = ''
    for i in range(0, len(value), 2):
        tmp = int(value[i:i + 2], 16)
        result += chr(tmp)
    return result