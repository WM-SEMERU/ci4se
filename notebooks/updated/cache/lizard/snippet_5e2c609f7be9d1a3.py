def merge_blocks(a_blocks, b_blocks):
    assert a_blocks[-1][2] == b_blocks[-1][2] == 0
    assert a_blocks[-1] == b_blocks[-1]
    combined_blocks = sorted(list(set(a_blocks + b_blocks)))
    i = j = 0
    for a, b, size in combined_blocks:
        assert i <= a
        assert j <= b
        i = a + size
        j = b + size
    return combined_blocks