def convert_to_strings(self, sequences, sizes=None):
    strings = []
    for x in xrange(len(sequences)):
        seq_len = sizes[x] if sizes is not None else len(sequences[x])
        string = self._convert_to_string(sequences[x], seq_len)
        strings.append(string)
    return strings