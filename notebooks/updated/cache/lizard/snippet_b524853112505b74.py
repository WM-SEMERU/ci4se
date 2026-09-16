def read_variant(variant):
    result = 0
    cnt = 0
    for data in variant:
        result |= (data & 127) << 7 * cnt
        cnt += 1
        if not data & 128:
            return result, variant[cnt:]
    raise Exception('invalid variant')