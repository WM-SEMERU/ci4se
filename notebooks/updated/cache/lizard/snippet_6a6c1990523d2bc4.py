def seek(self, pos):
    if pos > self.file_size or pos < 0:
        raise Exception('Unable to seek - position out of file!')
    self.file.seek(pos)