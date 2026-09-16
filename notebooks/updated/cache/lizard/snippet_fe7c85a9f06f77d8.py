def from_rows(Class, alphabet, rows):
    sorted_alphabet = sorted(alphabet)
    char_to_index = zeros(256, int16) - 1
    for i, ch in enumerate(sorted_alphabet):
        char_to_index[ord(ch)] = i
    values = zeros((len(rows), len(alphabet)), float32)
    for i, row in enumerate(rows):
        assert len(row) == len(alphabet)
        for ch, val in zip(alphabet, row):
            values[i, char_to_index[ord(ch)]] = val
    matrix = Class()
    matrix.alphabet = alphabet
    matrix.sorted_alphabet = sorted_alphabet
    matrix.char_to_index = char_to_index
    matrix.values = values
    return matrix