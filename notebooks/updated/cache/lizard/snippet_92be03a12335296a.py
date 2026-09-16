def read_file(self):
    with open(self.filename, mode='r+', encoding='utf8') as text_file:
        self.raw_file = text_file.read()
    self.file_lines = [x.rstrip() for x in self.raw_file.splitlines()]