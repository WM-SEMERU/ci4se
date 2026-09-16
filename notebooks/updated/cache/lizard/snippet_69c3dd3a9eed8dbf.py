def _step5(self, word):
    if word[-1] == 'e':
        a = self._m(word, len(word) - 1)
        if a > 1 or a == 1 and not self._cvc(word, len(word) - 2):
            word = word[:-1]
    if word.endswith('ll') and self._m(word, len(word) - 1) > 1:
        word = word[:-1]
    return word