def build(self, words):
    words = [self._normalize(tokens) for tokens in words]
    self._dawg = dawg.CompletionDAWG(words)
    self._loaded_model = True