def iter_filth(self, text):
    all_filths = []
    for detector in self._detectors.values():
        for filth in detector.iter_filth(text):
            if not isinstance(filth, Filth):
                raise TypeError('iter_filth must always yield Filth')
            all_filths.append(filth)
    all_filths.sort(key=lambda f: (f.beg, -f.end))
    if not all_filths:
        raise StopIteration
    filth = all_filths[0]
    for next_filth in all_filths[1:]:
        if filth.end < next_filth.beg:
            yield filth
            filth = next_filth
        else:
            filth = filth.merge(next_filth)
    yield filth