def generateSequence(self, text, preprocess=False):
    tokens = TextPreprocess().tokenize(text)
    cat = [-1]
    self.sequenceCount += 1
    uniqueID = 'q'
    data = self._formatSequence(tokens, cat, self.sequenceCount - 1, uniqueID)
    return data