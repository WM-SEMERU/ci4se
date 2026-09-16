def swap_word_order(source):
    assert len(source) % 4 == 0
    words = 'I' * (len(source) // 4)
    return struct.pack(words, *reversed(struct.unpack(words, source)))