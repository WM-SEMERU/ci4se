def encodeWord(self, word):
    encoded_word = word.encode(encoding=self.encoding, errors='strict')
    return Encoder.encodeLength(len(word)) + encoded_word