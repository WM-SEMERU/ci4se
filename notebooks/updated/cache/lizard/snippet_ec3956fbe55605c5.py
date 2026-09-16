def stem_word(self, p, i=0, j=None):
    if j is None and i == 0:
        word = p
    else:
        if j is None:
            j = len(p) - 1
        word = p[i:j + 1]
    if word in self.pool:
        return self.pool[word]
    if len(word) <= 2:
        return word
    word = self._step1ab(word)
    word = self._step1c(word)
    word = self._step2(word)
    word = self._step3(word)
    word = self._step4(word)
    word = self._step5(word)
    return word