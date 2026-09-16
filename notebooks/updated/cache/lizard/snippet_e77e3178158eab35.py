def _lemmatise_contractions(self, f, *args, **kwargs):
    fd = f
    for contraction, decontraction in self._contractions.items():
        if fd.endswith(contraction):
            fd = f[:-len(contraction)]
            if 'v' in fd or 'V' in fd:
                fd += decontraction
            else:
                fd += deramise(decontraction)
            yield from self._lemmatise(fd, *args, **kwargs)