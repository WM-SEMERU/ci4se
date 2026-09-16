def encode(self):
    if self.mode == tables.modes['alphanumeric']:
        encoded = self.encode_alphanumeric()
    elif self.mode == tables.modes['numeric']:
        encoded = self.encode_numeric()
    elif self.mode == tables.modes['binary']:
        encoded = self.encode_bytes()
    elif self.mode == tables.modes['kanji']:
        encoded = self.encode_kanji()
    return encoded