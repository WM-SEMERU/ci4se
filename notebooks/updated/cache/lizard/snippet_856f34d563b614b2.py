def load_from_file(self, fname):
    with open(fname, 'r') as f:
        for line in f:
            k, v = line.split(' = ')
            self._parse_char_line_to_self(k, v)