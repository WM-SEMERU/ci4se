def effective_len(self):
    if self._effective_len is None:
        self._effective_len = len([nuc for nuc in self.sequenceData if nuc !=
            'N' and nuc != 'n'])
    return self._effective_len