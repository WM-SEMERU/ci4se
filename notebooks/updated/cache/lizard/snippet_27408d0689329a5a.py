def read_entry(self):
    if not self._current_range:
        return None
    output = None
    while True:
        try:
            e = self._stream.next()
        except StopIteration:
            e = None
        if e:
            rng = e.range
            if not rng:
                raise ValueError(
                    'no range property. it is required in a locus stream')
            if rng.overlaps(self._current_range):
                self._current_range.payload.append(e)
                if self._current_range.end < rng.end:
                    self._current_range.end = rng.end
            else:
                output = self._current_range
                self._current_range = rng
                self._current_range.set_payload([e])
                break
        else:
            output = self._current_range
            self._current_range = None
            break
    return output