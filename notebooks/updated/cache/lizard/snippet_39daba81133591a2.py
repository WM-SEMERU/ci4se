def sounds_like(self, word1, word2):
    return self.phonetics(word1) == self.phonetics(word2)