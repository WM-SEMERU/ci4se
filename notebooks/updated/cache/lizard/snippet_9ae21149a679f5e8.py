def compare_hexdigests(digest1, digest2):
    digest1 = tuple([int(digest1[i:i + 2], 16) for i in range(0, 63, 2)])
    digest2 = tuple([int(digest2[i:i + 2], 16) for i in range(0, 63, 2)])
    bits = 0
    for i in range(32):
        bits += POPC[255 & digest1[i] ^ digest2[i]]
    return 128 - bits