def _lemmatise_assims(self, f, *args, **kwargs):
    forme_assimilee = self.assims(f)
    if forme_assimilee != f:
        for proposal in self._lemmatise(forme_assimilee, *args, **kwargs):
            yield proposal