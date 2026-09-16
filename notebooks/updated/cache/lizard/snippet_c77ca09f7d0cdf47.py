def counter(self, ch, part=None):
    return Counter(self(self._key(ch), part=part))