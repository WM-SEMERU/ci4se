def _consume_blanklines(self):
    empty_size = 0
    first_line = True
    while True:
        line = self.reader.readline()
        if len(line) == 0:
            return None, empty_size
        stripped = line.rstrip()
        if len(stripped) == 0 or first_line:
            empty_size += len(line)
            if len(stripped) != 0:
                err_offset = self.fh.tell() - self.reader.rem_length(
                    ) - empty_size
                sys.stderr.write(self.INC_RECORD.format(err_offset, line))
                self.err_count += 1
            first_line = False
            continue
        return line, empty_size