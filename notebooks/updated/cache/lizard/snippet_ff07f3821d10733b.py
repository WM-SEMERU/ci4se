def tag(self, *tag, **kwtags):
    if not tag:
        pass
    elif len(tag) == 1 and isinstance(tag[0], dict):
        self._meta.update(tag[0])
    else:
        raise TypeError(
            'Tags must be provided as key-word arguments or a dictionary')
    self._meta.update(kwtags)
    return self