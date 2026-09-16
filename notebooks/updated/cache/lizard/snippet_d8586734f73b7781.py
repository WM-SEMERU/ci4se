def load(self, filename, offset):
    try:
        self.offset = offset
    except IOError:
        self.logger.error('Unable to load EfiSystem volume')