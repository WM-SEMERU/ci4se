def tail(self, lines=10):
    self.seek_end()
    end_pos = self.file.tell()
    for i in range(lines):
        if not self.seek_line():
            break
    data = self.file.read(end_pos - self.file.tell() - 1)
    if data:
        return self.splitlines(data)
    else:
        return []