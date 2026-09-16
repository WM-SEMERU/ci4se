def SkipAhead(self, file_object, number_of_characters):
    lines_size = len(self.lines)
    while number_of_characters >= lines_size:
        number_of_characters -= lines_size
        self.lines = ''
        self.ReadLines(file_object)
        lines_size = len(self.lines)
        if lines_size == 0:
            return
    self.lines = self.lines[number_of_characters:]