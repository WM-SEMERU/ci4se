def conjugate(self, tense='present'):
    if self.tenses.has_key(tense):
        return self._extract(self.tenses[tense])
    elif self.tenses.has_key(tense.title()):
        return self._extract(self.tenses[tense.title()])
    return [None]