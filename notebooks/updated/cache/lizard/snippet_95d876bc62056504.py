def _line_iter(self, in_handle):
    reader = csv.reader(in_handle, dialect='excel-tab')
    for line in reader:
        if len(line) > 0 and line[0]:
            if line[0].upper() == line[0] and ''.join(line[1:]) == '':
                line = [line[0]]
            yield line