def replace(self, old, new, start=None, end=None, count=None, bytealigned=None
    ):
    old = Bits(old)
    new = Bits(new)
    if not old.len:
        raise ValueError('Empty bitstring cannot be replaced.')
    start, end = self._validate_slice(start, end)
    if bytealigned is None:
        bytealigned = globals()['bytealigned']
    if count is not None:
        count += 1
    sections = self.split(old, start, end, count, bytealigned)
    lengths = [s.len for s in sections]
    if len(lengths) == 1:
        return 0
    if new is self:
        new = copy.copy(self)
    positions = [lengths[0] + start]
    for l in lengths[1:-1]:
        positions.append(positions[-1] + l)
    positions.reverse()
    try:
        newpos = self._pos
        for p in positions:
            self[p:p + old.len] = new
        if old.len != new.len:
            diff = new.len - old.len
            for p in positions:
                if p >= newpos:
                    continue
                if p + old.len <= newpos:
                    newpos += diff
                else:
                    newpos = p
        self._pos = newpos
    except AttributeError:
        for p in positions:
            self[p:p + old.len] = new
    assert self._assertsanity()
    return len(lengths) - 1